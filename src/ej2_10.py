
def Ask_User():
    return int(input('Quieres una pizza vegetariana (1)/ pizza no vegetariana(2) -> '))

def Clasify(selection):
    match selection:
        case 1:
            return 'vegetariana'
        case 2:
            return 'no vegetariana'

def Elements(clasification):
    match clasification:
        case 'vegetariana':
            list = ['Pimiento (1)', 'tofu (2)']
            joinedList= ','.join(list)

            answer = int(input(f'Ingredientes vegetarianos: {joinedList} -> '))

            ingredient = list[answer-1].split(' ')

            return ingredient[0].lower()

        case 'no vegetariana':
            list = ['Peperoni (1)', 'Jamon (2)', 'Salmon (3)']
            joinedList= ','.join(list)

            answer = int(input(f'Ingredientes no vegetarianos: {joinedList} -> '))

            list = list[answer-1].split(' ')

            return (list[0]).lower()



def main():
    selection = Ask_User()
    clasification = Clasify(selection)
    chosenElement = Elements(clasification)

    print(f'\nTu pizza elegida es {clasification}')
    print(f'Los ingredientes son tomate, mozzarella, {chosenElement}')

if __name__ == "__main__":
    main()