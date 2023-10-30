from ej2_04 import Pedirnumeros

def Impar(number):
    for i in range(0,number+1):
        if i == number:
                print(i)

        elif i%2 != 0:
            print(i, end = ',')
        
def main():
    number = Pedirnumeros()
    Impar(number)

if __name__ == "__main__":
    main()
