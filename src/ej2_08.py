
def Score():
    return float(input('Introduce la puntuación del trabajador -> '))

def Level(score):
    if score == 0.0:
        return 'inaceptable'
    elif score == 0.4:
        return 'aceptable'
    elif score >= 0.6:
        return 'meritorio'
    else:
        return 'Fallaste'
    
def Earnings(score):
    return 2400*score

def main():
    mark = Score()
    level= Level(mark)
    score = int(Earnings(mark))

    if Level(mark) == 'Fallaste':
        print(level)
    else:
        print(f'El rendimiento del trabajador es {level} y recibira {score} euros')

if __name__ == '__main__':
    main()
