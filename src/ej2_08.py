
def Score():
    return float(input('Introduce la puntuación del trabajador -> '))

def Level(score):
    if score == 0.0:
        return 'inaceptable'
    elif score == 0.4:
        return 'aceptable'
    elif score >= 0.6:
        return 'meritorio'

def main():
    mark = Score()
    level= Level(mark)

    print(f'El rendimiento del trabajador es {level} y recibira {int(2400*mark)} euros')

if __name__ == '__main__':
    main()
