def Pedirnumeros():
    entrada = input('Numero -> ')
    numero = int(entrada)
    
    return numero

def Countdown(number):
    lista = ''
    for i in range (number,-1,-1):
        if i == 0:
            lista += str(i)
            return lista

        i_comma = str(i) + ','
        lista += i_comma

    return lista

def main():
    number = Pedirnumeros()
    print(Countdown(number))

if __name__ == "__main__":
    main()
