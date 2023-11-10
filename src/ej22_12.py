
def Ask_User():
    frase = input('Introduce una frase -> ')
    letra = input('Introduce una letra -> ')

    return frase,letra

def Countletter(frase,letra):
    counter = 0

    for i in range(0,len(frase)):
        if frase[i] == letra:
            counter += 1

    return counter

def main():
    frase,letra = Ask_User()
    counter = Countletter(frase,letra)

    if counter > 1:
        print(f'La letra aparece {counter} veces')
    else:
        print(f'La letra {letra} aparece {counter} vez')

if __name__ == "__main__":
    main()