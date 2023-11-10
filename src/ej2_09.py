
def AskAge():
    return int(input('Edad -> '))

def Clasify(Age):
    if Age < 4:
        return 'gratis'
    elif Age < 18:
        return '5'
    elif Age >= 18:
        return '10'
    
def main():
    Age = AskAge()

    Entrada = Clasify(Age)

    if Entrada == 'gratis':
        print('Puedes entrar gratis!')
    else:
        print(f'Tu entrada cuesta {Entrada} euros')

if __name__ == "__main__":
    main()