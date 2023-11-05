
def User_input():
    return input('Introduce una palabra -> ')

def Input_Loop(word):
    loop = ''
    word_comma = word + ','
    for i in range(1,10):
        loop += word_comma

        if i == 9:
            loop += word

    return loop 

def main():
    word = User_input()
    print(Input_Loop(word))

if __name__ == "__main__":
    main()