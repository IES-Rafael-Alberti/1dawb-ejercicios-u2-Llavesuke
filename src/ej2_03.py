def PedirNumeros():
    num1 = input('Numero 1 -> ')
    num2 = input('Numero 2 -> ')

    return num1,num2

def division(num1:int,num2:int):
    if num1%num2 == 0:
        resultado = num1/num2

        print(resultado)

        return resultado
    
    else: 
        print('Error')
        return 'Error'

def main():
    num1,num2 = PedirNumeros()
    division(int(num1),int(num2))

if __name__ == "__main__":
    main()