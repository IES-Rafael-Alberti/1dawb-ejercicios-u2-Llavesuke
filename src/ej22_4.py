from ej2_04 import Pedirnumeros

def Countdown(number):
    for i in range (number,-1,-1):
        if i == 0:
            print(i)
        print(i, end = ',')

def main():
    number = Pedirnumeros()
    Countdown(number)

if __name__ == "__main__":
    main()
