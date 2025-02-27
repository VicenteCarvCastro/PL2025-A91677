# TPC3 - Conversor MarkDown para HTML

**Data:** 2025-02-26  
**Autor:** Vicente de Carvalho Castro  
**Número:** A91677  

<img src="../foto_perfil.png" alt="Foto do Autor" width="150"/>

---

## Resumo
Este trabalho consistiu em desenvolver um programa que converte um ficheiro MarkDown (`textoMD.md`) para HTML (`saida.html`).

O programa lê o arquivo linha-a-linha, aplicando transformações específicas para diferentes elementos de Markdown, como cabeçalhos, negrito, itálico, links, imagens e listas numeradas.
Para cada sintaxe MarkDown tinha uma função específica que convertia na expressão pela correspondente em HTML, usei expressões regulares para este processo, nomeadamente da funçao `re.sub` para substituir os elementos.

A principal dificuldade foi o tratamento das listas numeradas. Como os itens aparecem consecutivamente, decidi criar uma lista temporária `list_buffer` para agrupar itens de lista numerada antes de convertê-los para HTML. Garantindo que a lista seja fechada corretamente com `<ol>`.

## Resultados
Os seguintes ficheiros foram gerados durante a realização deste TPC:  
- [`conversor.py`](conversor.py) - Código desenvolvido  
- [`textoMD.md`](textoMD.md) - Ficheiro em MarkDown para conversão
- [`saida.html`](saida.html) - Ficheiro de saída convertido