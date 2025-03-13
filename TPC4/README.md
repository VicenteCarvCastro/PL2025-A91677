# TPC4 - Analisador Léxico

**Data:** 2025-03-06  
**Autor:** Vicente de Carvalho Castro  
**Número:** A91677  

<img src="../foto_perfil.png" alt="Foto do Autor" width="150"/>

---

## Resumo
Este trabalho pediu a construção de um analisador léxico para uma liguagem de query com a qual se podem escrever frases

- Definição de Tokens (`token_specification`)
Uma lista de tuplos  que especifica os tipos de tokens e suas expressões regulares correspondentes. Nomeadamente, 'KEYWORD', 'VARIABLE', 'IDENTIFIER', entre outros..

- Processo de Análise Léxica
Depois todas as expressões regulares são compiladas e atribuídas à variável `token_regex`
Ignora espaços em branco e gera erro se encontrar um caractere inesperado
Retorna uma lista de tokens no formato `(TIPO, VALOR)`.



## Resultados
Os seguintes ficheiros foram gerados durante a realização deste TPC:  
- [`analisador.py`](analisador.py) - Código desenvolvido  
- [`result.png`](result.png) - Print do resultado do programa com a query exemplo dada,  imprimido no terminal