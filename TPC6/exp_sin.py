import ply.yacc as yacc
from exp_lex import tokens, literals

def p_Sexp(p): 
    "SExp : Exp"
    p[0] = p[1]
    print(f"Valor: {p[0]}")


def p_Exp(p): 
    "Exp : Termo Exp2"
    p[0] = p[1] + p[2]

def p_Exp2_add(p):
    "Exp2 : '+' Termo Exp2"
    p[0] = p[2] + p[3]  # Soma com o próximo termo

def p_Exp2_sub(p):
    "Exp2 : '-' Termo Exp2"
    p[0] = -p[2] + p[3]  # Subtrai e continua

def p_Exp2_empty(p):
    "Exp2 : "  # Regra vazia para evitar recursão infinita
    p[0] = 0

# Multiplicação e divisão (associatividade à esquerda)
def p_Termo(p):
    "Termo : Fator Termo2"
    p[0] = p[1] * p[2]

def p_Termo2_mult(p):
    "Termo2 : '*' Fator Termo2"
    p[0] = p[2] * p[3]

def p_Termo2_div(p):
    "Termo2 : '/' Fator Termo2"
    p[0] = (1 / p[2]) * p[3]  # Inverso para evitar erro com divisão

def p_Termo2_empty(p):
    "Termo2 : "  
    p[0] = 1

# Parênteses e números
def p_Fator_exp(p):
    "Fator : '(' Exp ')'"
    p[0] = p[2]

def p_Fator_num(p):
    "Fator : num"  
    p[0] = int(p[1]) 

# Tratamento de erro
def p_error(p):
    if p:
        print(f"Erro sintático perto de '{p.value}', linha {p.lineno}")
    else:
        print("Erro sintático: fim inesperado da entrada")
    parser.success = False
    
# Construir o parser
parser = yacc.yacc(debug=True)


import sys
for linha in sys.stdin:
    parser.success = True
    parser.parse(linha)
    if parser.success:
        print("Frase válida: ", linha)
    else:
        print("Frase inválida.. Corrija e tente novamente")





