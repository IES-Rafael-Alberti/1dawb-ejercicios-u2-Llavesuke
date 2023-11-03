
def Mount_quantity():
    numeroBuscado = False
    TotalVenta = 0

    while not numeroBuscado:
        entrada = int(input('Ingresa monto | Para salir ingrese 0 -> '))

        if entrada == 0:
            numeroBuscado = True
        elif entrada < 0:
            print('Ingresa un nuevo monto\n')
        else: 
            TotalVenta += entrada

    return TotalVenta


def main():
    venta = Mount_quantity()

    if venta > 1000:
        print(f'Tiene que pagar {venta-(venta*0.1)}')
    else: 
        print(f'Tiene que pagar {venta} euros')

if __name__ == "__main__":
    main()