
def somador():
    acc = 0
    ligado = True
    f = open("texto.txt")
    for linha in f:
        for char in linha.split():
            if char.isdigit():
                print("char: " + char)
                if ligado:
                    acc = acc + int(char)
                    print(acc)
                    print("----")
            elif char.lower() == 'off':
                ligado = False
            elif char.lower() == 'on':
                ligado = True
            elif char == '=':
                print(acc) 
    f.close()

somador()