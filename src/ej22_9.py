from ej2_02 import ask_password

def compare_password(password):
    saved_password = 'contraseña'

    while saved_password != password:
        password = input('Introduce la contraseña guardada: ').lower()

    print('Has introducido la contraseña correcta ')

def main():
    password = ask_password
    compare_password(password)

if __name__ == "__main__":
    main()