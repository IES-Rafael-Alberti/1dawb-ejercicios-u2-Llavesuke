def Pedirnumeros():
    entrada = input('Numero -> ')
    numero = int(entrada)
    
    return numero

def par_impar(numero:int):
    if numero%2 == 0:
        return True
    
    else:
        return False    
    
def main():
   numero= Pedirnumeros()
   if par_impar(numero):
    print('El número es par')
   else:
      print('El número es impar')


if __name__ == "__main__":
    main()