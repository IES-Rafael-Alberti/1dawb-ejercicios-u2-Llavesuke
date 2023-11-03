from ej2_04 import Pedirnumeros

def Sum(numero:int):
    mayor = None

    while numero != 0:
        print(numero)

        if mayor is None or numero > mayor:
            mayor = numero

        numero = int(input('Introduce otro numero o 0 para salir del programa -> '))

    print(f'\nEl numero mayor es {mayor}')

def main():
    numero = Pedirnumeros()
    Sum(numero)

if __name__ == "__main__":
    main()
