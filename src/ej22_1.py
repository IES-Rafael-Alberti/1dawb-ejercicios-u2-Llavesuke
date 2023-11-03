
def PedirNumeros():
    return input('Introduce una palabra -> ')

def Input_Loop(word):
    for i in range(1,11):
        print(word, end = ',')
        if i == 10:
            print(f'{word}\n')

def main():
    word = PedirNumeros()
    Input_Loop(word)

if __name__ == "__main__":
    main()