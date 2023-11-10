
def Ask_User():

    invest_amount = int(input('Cantidad a invertir -> '))
    anual_interest = int(input('Interes anual -> '))
    years = int(input('Cuantos años tiene previsto de inversion -> '))

    return invest_amount, anual_interest, years

def Inversion(invest_amount, anual_interest,years):
    for i in range (1,years+1):
        invest_amount *=  (i + anual_interest/100)
        
        print('Año',i, '=' '{:.2f}'.format(invest_amount))
        
def main():
    invest_amount,anual_interest,years = Ask_User()

    Inversion(invest_amount, anual_interest,years)

if __name__ == "__main__":
    main()