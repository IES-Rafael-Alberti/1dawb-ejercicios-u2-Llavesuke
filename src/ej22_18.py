from ej22_17 import User_Input

def Par(numero):
    par = 0
    if int(numero)%2 == 0:
            par += 1

    return par

def Digit_Sum(numero):
    par = 0
    while int(numero) != -1: 
        suma = 0

        for i in range(0,len(numero)):
            suma += int(numero[i])
        
        par += Par(numero)
            
        print(f'\nLa suma de los digitos es {suma}')

        numero = User_Input()
    
    return par


    

def main():
    numero = User_Input()
    par = Digit_Sum(numero)
    if par == 1:
        print(f'Se han introducido {par} numero par')
    else:
         print(f'Se han introducido {par} numeros pares')
         
if __name__ == "__main__":
    main()