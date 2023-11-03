
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

def menu(entrada):
    match entrada:
        case 1:
            print('Has elegido la opción 1')
        case 2:
            print('Has elegido la opcion 2')
        case 3:
            return 'Adios'

def main():
   entrada = Selection()
   menu(entrada)


if __name__ == "__main__":
    main()