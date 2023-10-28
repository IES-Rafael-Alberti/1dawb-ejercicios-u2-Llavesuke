
def ask_password():

    entrada = input('Contraseña -> ')
    contraseña_usuario = entrada.lower()
    return contraseña_usuario

def compare_password(contraseña_usuario):

    contraseña_guardada = 'contraseña'

    if contraseña_guardada == contraseña_usuario:
        return True
    else:
        return False

def main():
    contraseña_usuario = ask_password()
    
    if compare_password(contraseña_usuario):
        print('\nHas iniciado sesion!')
    else:
        print('\nContraseña erronea')


if __name__ == "__main__":
    main()