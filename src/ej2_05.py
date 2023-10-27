
def ask_age():
    entrada = input('Edad -> ')
    age = int(entrada)

    return age

def ask_salary():
    entrada = input('Salario mensual -> ')
    salary = int(entrada)

    return salary

def verify(age, salary):
    if age >= 16 and salary >= 1000:
        return True
    else:
        return False
    
def main():
    age = ask_age()
    salary = ask_salary()

    if verify(age,salary):
        print ('Tienes que tributar')
    else:
        print('No tienes que tributar este año')

if __name__ == "__main__":
    main()  
