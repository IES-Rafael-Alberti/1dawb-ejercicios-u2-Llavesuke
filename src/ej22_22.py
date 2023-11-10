def User_Input():
    entrada = input('Numero -> ')
    return entrada

def Par_impar(numero):
    par = 0
    impar = 0

    for i in range(0,len(numero)):
        if int(numero[i])%(2) == 0:
            par += 1
        else:
            impar += 1

    return par, impar


def main():
    contador_par = 0
    contador_impar = 0 
    numerobuscado = False

    while not numerobuscado:
        entrada = User_Input()

        if int(entrada) == 0:
            numerobuscado = True
        else:

            par, impar = Par_impar(entrada)

            contador_par += par
            contador_impar += impar
    
    print(f'Hay {contador_impar} impares y {contador_par} pares ')
if __name__ == "__main__":
    main()