def tabla():
    numero = 1
    while numero != 11:
        print(f'\nTabla {numero}')
        for i in range(1,11):
            print(f'{numero}*{i} = {numero*i}')
        numero += 1

def main():
    tabla()

if __name__ == "__main__":
    main()