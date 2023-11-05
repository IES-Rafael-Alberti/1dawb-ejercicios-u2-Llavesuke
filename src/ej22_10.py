from ej2_04 import Pedirnumeros

def Primo(numero):
    for i in range (2,numero):
        if numero%i == 0:
            return False
        else:
            return True
    if numero == 1:
        return True
    
def main():
    numero = Pedirnumeros()
    if Primo(numero):
        print('Es primo')
    else:
        print('No es primo')

if __name__ == "__main__":
    main()