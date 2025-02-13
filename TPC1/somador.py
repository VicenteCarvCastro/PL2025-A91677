import sys

acc = 0
ligado = True

for linha in sys.stdin:
    for word in linha.split():
        # Primeiro verifica os comandos antes de tentar processar números
        if word.lower() == 'off':
            ligado = False
            continue
        elif word.lower() == 'on':
            ligado = True
            continue
        elif word == '=':
            print("Resultado:", acc)
            continue
        
        # Apenas processa números se estiver ligado
        if ligado:
            i = 0
            while i < len(word):
                num_str = ""

                # Extrai um número da palavra
                while i < len(word) and word[i].isdigit():
                    num_str += word[i]
                    i += 1  # Avança enquanto for um dígito

                # Se encontrou um número válido, soma-o
                if num_str:
                    acc += int(num_str)
                    print("Número encontrado:", num_str)
                    print("Acc:", acc)

                # Avança para o próximo caractere não numérico
                i += 1  # Para evitar loop infinito em caracteres não numéricos
