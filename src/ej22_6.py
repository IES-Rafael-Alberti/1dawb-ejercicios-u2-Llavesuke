from ej2_04 import Pedirnumeros

def Piramide(numero):
    for i in range(1, numero+1):
        print('*'*i)

def main():
    numero = Pedirnumeros()
    Piramide(numero)

if __name__ == "__main__":
    main()