# Lista de compras donde el usuario ingresa productos a comprar y si lo desea los puede eliminar
#
#
#
#

# Creación de la lista de compras vacía.
mi_lista = []

while True:

    # Impresión del mensaje de bienvenida
    print('=' * 30)
    print('1. Agregar un producto')
    print('2. Eliminar un producto')
    print('3. Ver Lista')
    print('4. Salir')
    print('=' * 30)

    # Almacenamiento de datos que ingresará el usuario
    opcion = input('Qué deseas hacer?: ')

    # Preguntar al usuario que desea hacer mostrando el menú
    #
    #
    # Opción 1
    if opcion == '1':
        producto = input('Ingresa el nombre del producto: ')
        mi_lista.append(producto)
        print(f'Producto {producto} agregado a la lista de compras')
    elif opcion == '2':
        if mi_lista:
            print('Lista de productos: ')
            for i, producto in enumerate(mi_lista, 1):
                print(f'{i}, {producto}')
    elif opcion == '3':
        if mi_lista:
            print(f'Lista de productos:')
            for i, producto in enumerate(mi_lista, 1):
                print(f'{i}. {producto}')
        else:
            print('La lista está vacía.')
    elif opcion == '4':
        print('Hasta luego!')
        break
    else:
        print('Opcíon inválida. Intenta nuevamente.')