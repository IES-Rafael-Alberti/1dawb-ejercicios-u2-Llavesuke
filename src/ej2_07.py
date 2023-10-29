
def UserRent():
    entrada = input('Introduzca su renta anual -> ')
    rent = int(entrada)

    return rent

def SelectPercentage(rent:int):
    if rent < 10000:
        return 5
    elif rent < 20000:
        return 15
    elif rent < 35000:
        return 20
    elif rent <= 60000:
        return 30
    elif rent > 60000:
        return 45

def main():
    rent = UserRent()
    percentage = SelectPercentage(rent)

    print(f'Tu renta anual es {rent} y te corresponde un porcentaje de {percentage}%' )

if __name__ == "__main__":
    main()