import sys
import re
import unicodedata

# Função para extrair sobrenome e nome
def extrair_sobrenome_nome(compositor):
    if ", " in compositor:
        # Formato "Sobrenome, Nome"
        sobrenome, nome = compositor.split(", ", 1)
        return (sobrenome, nome)
    else:
        # Formato "Nome Sobrenome"
        partes = compositor.split()
        sobrenome = partes[-1]  # Última palavra é o sobrenome
        nome = " ".join(partes[:-1])  # Restante é o nome
        return (sobrenome, nome)
    

def add_tuplo_lista(lista, periodo):
  i = 0
  while i < len(lista) and lista[i][0] != periodo:
    i += 1
    
  # Se encontrou o período, atualiza o contador criando um novo tuplo
  if i < len(lista):
    #print("JA EXISTE ")
    p, count = lista[i]
    lista[i] = (p, count + 1)
        
  else:
    print("Vou criar um novo tuplo com: ", periodo)
    novo_tuplo = tuple([periodo,1])
    lista.append(novo_tuplo)



# ------- Main -------


buffer = ""
titulo = ""
compositores = []
lista_periodos = []

dict_periodo = {}



f = open("obras.csv")
next(f)
for linha in f:
  buffer += linha # "Itera" ate chegar a ultima linha de definicao da obra 

  ult_linha = re.match(r'.*(?=;\d{4})(.*)', linha) #group(0) -> descricao / group(1) -> resto
  inicio = re.match(r'^\w[^;]+', linha)
  

  if inicio:
     titulo = inicio.group()
     print("Titulo: ", titulo)

  if ult_linha: # estou na ultima linha da obra no csv
    print("Titulo if ult_linha: ", titulo)
    
    resto_linha = re.match(r'^;([^;]*);([^;]*);([^;]*);([^;]*);(O\d+)', ult_linha.group(1)) # para extrair resto dos parametros (3..7)
    if resto_linha:

      compositores.append(resto_linha.group(3))
      
      periodo = resto_linha.group(2)
      add_tuplo_lista(lista_periodos, periodo)

      if periodo not in dict_periodo:
        dict_periodo[periodo] = []  
      dict_periodo[periodo].append(titulo)

      titulo = ""
      buffer = ""


    
  inteira = re.match(r'^([^;]*);([^;]*);([^;]*);([^;]*);([^;]*);([^;]*);(O\d+)$', linha)
  
  if inteira:

    #Adicionar compositor a lista
    compositores.append(inteira.group(5))

    periodo = inteira.group(4)
    titulo2 = inteira.group(1)
    add_tuplo_lista(lista_periodos, periodo)
    
    if periodo not in dict_periodo:
      dict_periodo[periodo] = []  
    dict_periodo[periodo].append(titulo2)
       

    buffer=""


compositores_unicos = list(set(compositores))

compositores_ordenados = sorted(compositores_unicos, key=extrair_sobrenome_nome)

print("------ Lista Compositores --------- \n")
for compositor in compositores_ordenados:
    print(compositor)
 

print("---------- Disribuicao Obras por Periodo --------- \n")
for (p,q) in lista_periodos:
   print(p + ":" + str(q))

print("-------- Dicionario Periodos - Obras ---------- \n")
for periodo, titulos in dict_periodo.items():
    print(f"{periodo}:")
    for titulo in titulos:
        print(f"  - {titulo}")

f.close()   

