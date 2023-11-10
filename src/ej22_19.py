
def Selection():

    entrada = 0
    while entrada > 3 or entrada < 1:
        print('-------------------')
        print('Elige una opción')
        print(' 1. Comenzar programa \n 2. Imprimir listado \n 3.Finalizar el programa')
        print('-------------------')

        entrada = int(input(' -> '))

        if entrada > 3 or entrada < 1:
            print('Te has equivocado\n')
    
    return entrada

def menu():
    lista = ''
    entrada = None

    while entrada != 3 or entrada is None:
        entrada = Selection()
        
        match entrada:
            case 1:
                nota = input('Introduce una nota -> ') + '\n'
                lista += nota
            case 2:
             print('\n'+lista)
            case 3:
                print('Adios')
                return 3

def main():


    menu()


if __name__ == "__main__":
    main()