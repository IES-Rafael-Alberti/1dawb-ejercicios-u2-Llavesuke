from ej2_04 import Pedirnumeros

def Numero_filas(numero):
    variable = 1
    
    for i in range(1,numero+1):
        variable += 2
    return variable
 
def Fila(valor_fila):
    while valor_fila != 1:
            valor_fila -= 2
            print (valor_fila, end = ' ')
    print('')

def main():
    numero = Pedirnumeros()

    contador = 0

    while contador != numero+1:
        valor_fila = Numero_filas(contador)
        Fila(valor_fila)
        contador += 1

if __name__ == "__main__":
    main()
