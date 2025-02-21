# TPC2 - Análise Dataset Obras Musicais

**Data:** 2025-02-20  
**Autor:** Vicente de Carvalho Castro  
**Número:** A91677  

<img src="../foto_perfil.png" alt="Foto do Autor" width="150"/>

---

## Resumo
Este trabalho consistiu em ler e processar um dataset sem recurso ao módulo CSV do Python. Foram pretendidas 3 tarefas principais:
- Lista ordenada alfabeticamente dos compositores musicais
- Distribuição das obras por período: quantas obras catalogadas em cada período. Aqui usei uma lista de tuplos
- Dicionário em que a cada período está a associada uma lista alfabética dos títulos das obras
desse período.
- `Procedimento para a minha resolução` 

Primeiramente, o ficheiro csv fornecido continha linhas com multiplas espaços ou e tabs, o que dificultava a leitura do ficheiro linha a linha. Para isso usei um buffer em forma de 'string' para me ajudar na iteração das linhas do ficheiro. Utilizei também expressões regulares para facilitar no processo de  manipulação das linhas. Dividi em 2 casos particulares: 
    
Quando uma obra estava completamente definida numa só linha (chamei a expressão regular de `"inteira"` : `r'^([^;]*);([^;]*);([^;]*);([^;]*);([^;]*);([^;]*);(O\d+)$'`)

E o caso da ultima linha de definição da obra que gerlalmente começava com tabs e continuação da linha anterior (chamei a expressão regular de `"ult_linha"` : `(r'.*(?=;\d{4})(.*)`)

Outro aspeto importante que deu alguma dificuldade foi na divisão dos parâmetros usando `;`, devido ao 2ª parametro também haver a possibilidade de este caracter também estar presente na descrição. Para resolver isso, usei outra expressão regular (resto_linha: `r'^;([^;]*);([^;]*);([^;]*);([^;]*);(O\d+)` seguidamente `da ult_linha`). Ignorando assim o 2º parametro visto que não era necessário. Depois foi simplesmente guardar os parâmetros usando a funcionalidade `group()` do objeto Match das expressões regulares 
    

## Resultados
Os seguintes ficheiros foram gerados durante a realização deste TPC:  
- [`obras.py`](somador.py) - Código desenvolvido  
- [`obras.csv`](obras.csv) - Dataset fornecido