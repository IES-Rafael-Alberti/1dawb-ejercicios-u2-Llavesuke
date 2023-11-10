
def Book_Title():
    lista = ''
    entrada = ''
    linea = 0
    while entrada != '*':
        entrada = input('Libro: ')
        if entrada == '/':
            contador = Count_digits(lista)

            print(f'Linea completa. Aparecen {contador} dígitos númericos')
            linea += 1

            lista = ''
            contador = 0

        else:
            lista += entrada
    print(f'Se leyeron {linea} líneas completas.')

def Count_digits(lista):
    contador = 0
    for i in range (0, len(lista)):
        if lista[i].isnumeric():
            contador += 1
            
    return contador

def main():
    Book_Title()
    

if __name__ == "__main__":
    main()