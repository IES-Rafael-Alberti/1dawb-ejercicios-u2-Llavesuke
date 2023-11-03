from ej22_1 import PedirNumeros

def eco(entrada):
    while entrada.lower() != 'salir':
        print(f'-{entrada}-')
        entrada = input('Introduce una palabra -> ')

    print('Saliste del programa')

def main():
    entrada = PedirNumeros()
    eco(entrada)

if __name__ == "__main__":
    main()
