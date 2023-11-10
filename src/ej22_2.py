
def AskAge():
    return int(input('Edad -> '))

def Age_Sucesion(age):
    lista = ''

    for i in range (0,age+1):

        if i < age:
            i_comma = str(i) + ','
            lista += i_comma

        if i == age:
            lista += str(i)

    return lista

def main():
    age = AskAge()
    print(Age_Sucesion(age))

if __name__ == "__main__":
    main()