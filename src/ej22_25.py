
def User_input():
    return input('Introduce una frase -> ')

def largest_word(entrada):
    phrase = entrada.split(' ')
    palabra = phrase[0]

    for word in range (0,len(phrase)):

        if len(palabra) < len(phrase[word]):
            palabra = phrase[word]
            
        elif len(palabra) == len(phrase[word]):
            palabra = palabra

    return palabra,word+1

def main():
    entrada = User_input()
    palabra, word = largest_word(entrada)

    print(f'La palabra más larga es {palabra} | Habia {word} palabras')

if __name__ == "__main__":
    main()