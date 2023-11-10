

def AskName():
    return (input('Ponga su nombre -> ').upper())[0:1]

def AskSex():
    sex = input('Cual es su sexo (M|F) -> ').upper()
    
    return sex

def AssignGroup(name,sex):
    if (sex == 'M' and name >= 'N') or (sex == 'F' and name < 'M'):
        return True
    else:
        return False

def main():
    name = AskName()
    sex = AskSex()

    if AssignGroup(name,sex):
        print('Eres del grupo A')
    else:
        print('Eres del grupo B')

if __name__ == '__main__':
    main()