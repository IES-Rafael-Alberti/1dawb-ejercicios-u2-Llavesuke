from ej22_1 import User_input

def eco(entrada):
    while entrada.lower() != 'salir':
        print(f'-{entrada}-')
        entrada = input('Introduce una palabra -> ')

    print('Saliste del programa')

def main():
    entrada = User_input()
    eco(entrada)

if __name__ == "__main__":
    main()
