from ej2_09 import AskAge

def Age_Sucesion(age):
    for i in range (0,age+1):
        print(i, end = ',')
        if i == age:
            print(f'{i}\n')


def main():
    age = AskAge()
    Age_Sucesion(age)

if __name__ == "__main__":
    main()