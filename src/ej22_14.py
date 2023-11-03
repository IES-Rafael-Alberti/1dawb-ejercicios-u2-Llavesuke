from ej2_04 import Pedirnumeros

def Sum(numero:int):
    resultado = 0

    while numero != 0:
        print(numero)

        resultado += numero

        numero = int(input('Introduce otro numero o 0 para salir del programa -> '))

    print(f'\nLa suma de los numeros introducidos es {resultado}')

def main():
    numero = Pedirnumeros()
    Sum(numero)

if __name__ == "__main__":
    main()
