from ej22_10 import Primo
def PedirNumero():
    number = None
    lista = ''

    while number is None or number != '0':
        number = input('Numero -> ')

        if number.isnumeric() < 1:
            print('Numero no válido')
        if number == '0':
            return lista
        
        else: 
            number += ' '
            lista += number

    return lista

def main():
    cantidad_primos = 0

    lista_numeros = PedirNumero()

    lista_numeros = lista_numeros.split(' ')

    for i in range(0,(len(lista_numeros)-1)):
        if Primo(int(lista_numeros[i])):
            cantidad_primos += 1
    
    print(f'Hay {cantidad_primos} números primos en los que usted ha introducido')

if __name__ == "__main__":
    main()