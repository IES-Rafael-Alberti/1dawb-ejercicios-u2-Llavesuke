
def User_Input():
    return input('Introduce un número -> ')

def Digit_Sum(numero):
    suma = 0
    for i in range(0,len(numero)):
        suma += int(numero[i])

    return suma

def main():
    numero = User_Input()
    suma = Digit_Sum(numero)
    
    print(f'\nLa suma de los digitos es {suma}')
    
if __name__ == "__main__":
    main()