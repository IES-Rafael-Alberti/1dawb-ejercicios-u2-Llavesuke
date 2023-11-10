from ej22_12 import Ask_User

def Countletter(frase,letra):
 
    for i in range(0,len(frase)):
        if frase[i] == letra:
            print(f'Se ha encontrado la letra en la posición {i} de la frase')
        else:
            print(f'No se ha encontrado la letra en la posición {i} de la frase')


def main():
    frase,letra = Ask_User()
    Countletter(frase,letra)

if __name__ == "__main__":
    main()