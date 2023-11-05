def Pedirnumeros():
    entrada = input('Numero -> ')
    numero = int(entrada)
    
    return numero


def Impar(number):
    lista = ''

    for i in range(0,number):
        if i == number-1:
                lista += str(i)

        elif i%2 != 0:
            i_comma = str(i) + ','
            lista += i_comma

    return lista

def main():
    number = Pedirnumeros()
    print(Impar(number))

if __name__ == "__main__":
    main()
