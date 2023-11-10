def Pedirnumeros():
    entrada = input('Numero -> ')
    numero = int(entrada)
    
    return numero


def Piramide(numero):
    lista = ''
    for i in range(1, numero+1):
        lista += str('*'*i+'\n')
    
    return lista

def main():
    numero = Pedirnumeros()
    print(Piramide(numero))

if __name__ == "__main__":
    main()