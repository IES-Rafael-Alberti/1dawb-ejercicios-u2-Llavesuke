def PedirNumeros():
    return input('Introduce una palabra -> ')

def Wordbyword(word):
    lista = ' '
    for i in range(0,len(word)):
        lista += word[i] + '\n'
    lista = lista[::-1]
    
    return lista

def main():
    word = PedirNumeros()
    print(Wordbyword(word))

if __name__ == "__main__":
    main()