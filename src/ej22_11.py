from ej22_1 import PedirNumeros

def Wordbyword(word):
    lista = ' '
    for i in range(0,len(word)):
        lista += word[i] + '\n'
    print(f'{lista[::-1]}\n')

def main():
    word = PedirNumeros()
    Wordbyword(word)

if __name__ == "__main__":
    main()