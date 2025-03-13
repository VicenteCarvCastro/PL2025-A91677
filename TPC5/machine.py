import ply.lex as lex
import json
import sys

STOCK_FILE = "stock.json"
MOEDAS_VALIDAS = {"2e": 200, "1e": 100, "50c": 50, "20c": 20, "10c": 10, "5c": 5, "2c": 2, "1c": 1}

tokens = (
    'LISTAR',
    'MOEDA',
    'SELECIONAR',
    'SAIR',
    'CODIGO',
    'NUM',
    'MOEDA_TIPO'
)

t_ANY_ignore = ' \t\n'

def carregar_stock():
    try:
        with open(STOCK_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def guardar_stock(stock):
    with open(STOCK_FILE, "w", encoding="utf-8") as f:
        json.dump(stock, f, indent=4)

def listar_produtos(stock):
    print("cod | nome | quantidade | preço")
    print("---------------------------------")
    for produto in stock:
        print(f"{produto['cod']} {produto['nome']} {produto['quant']} {produto['preco']}e")

def t_LISTAR(t):
    r'LISTAR'
    listar_produtos(t.lexer.stock)

def t_MOEDA(t):
    r'MOEDA'
    return t

def t_SELECIONAR(t):
    r'SELECIONAR'
    return t

def t_CODIGO(t):
    r'[A-Z]\d{2}'
    return t

def t_SAIR(t):
    r'SAIR'
    troco = calcular_troco(t.lexer.saldo)
    if troco:
        troco_str = ", ".join([f"{v}x {k}" for k, v in troco.items()])
        print(f"maq: Pode retirar o troco: {troco_str}.")
    print("maq: Até à próxima")
    guardar_stock(t.lexer.stock)
    sys.exit()

def t_ANY_error(t):
    t.lexer.skip(1)

def calcular_troco(saldo):
    troco = {}
    for moeda, valor in sorted(MOEDAS_VALIDAS.items(), key=lambda x: -x[1]):
        while saldo >= valor:
            saldo -= valor
            troco[moeda] = troco.get(moeda, 0) + 1
    return troco

def processar_selecao(codigo, saldo, stock):

    produto = next((p for p in stock if p['cod'] == codigo), None)
    if not produto:
        print(f"maq: Produto {codigo} não encontrado.")
        return saldo, stock

    preco_total = produto['preco'] * 100  
    if saldo < preco_total:
        print(f"maq: Saldo insuficiente para satisfazer o seu pedido")
        print(f"maq: Saldo = {saldo // 100}e {saldo % 100}c; Pedido = {preco_total // 100}e {preco_total % 100}c")
        return saldo, stock

    if produto['quant'] <= 0:
        print(f"maq: Produto {codigo} esgotado.")
        return saldo, stock

    produto['quant'] -= 1
    saldo -= preco_total
    print(f"maq: Pode retirar o produto dispensado \"{produto['nome']}\"")
    print(f"maq: Saldo = {saldo // 100}e {saldo % 100}c")
    return saldo, stock


def main():

    print("maq: Bom dia. Estou disponível para atender o seu pedido.")
    
    lexer = lex.lex()
    lexer.saldo = 0
    lexer.stock = carregar_stock()

    for linha in sys.stdin:
        lexer.input(linha)  
        for tok in lexer:

            if tok.type == "MOEDA":
                moedas = linha.split('MOEDA')[1].strip()
                print(f">> MOEDA {moedas}")
                for moeda in moedas.split(', '):
                    lexer.saldo += MOEDAS_VALIDAS[moeda]
                print(f"maq: Saldo = {lexer.saldo // 100}e {lexer.saldo % 100}c")
           
            elif tok.type == 'SELECIONAR':
                tok = lexer.token()  
                if tok and tok.type == 'CODIGO':
                    codigo = tok.value
                    lexer.saldo, lexer.stock = processar_selecao(codigo, lexer.saldo, lexer.stock)

if __name__ == "__main__":
    main()