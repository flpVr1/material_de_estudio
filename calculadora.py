# Calculadora sencilla
#
#
#
#
# Inicio del bucle
while True:
    # Mensaje de bienvenida
    print('=' * 30)
    print('Bienvenido a la calculadora sencilla')
    print('\n¿Qué deseas hacer?')
    print('1. Sumar')
    print('2. Restar')
    print('3. Multiplicar')
    print('4. Dividir')
    print('5. Salir')
    seleccion_usuario = input('\nIngresa una opción: ')
    print('=' * 30)
    
    #Opción 1: Sumar
    if seleccion_usuario == '1':
        numero1 = int(input('Ingresa el primer número a sumar: '))
        numero2 = int(input('Ingresa el segundo número a sumar: '))
        resultado = numero1 + numero2
        print(f'El resultado de la suma de los números {numero1} y {numero2} es: {resultado}') 
    #Opción 2: Restar    
    elif seleccion_usuario == '2':
        numero1 = int(input('Ingresa el primer número a restar: '))
        numero2 = int(input('Ingresa el segundo número a restar: '))
        resultado = numero1 - numero2
        print(f'El resultado de la resta de los números {numero1} y {numero2} es: {resultado}')
    #Opción 3: Multiplicar
    elif seleccion_usuario == '3':
        numero1 = int(input('Ingresa el primer número a multiplicar: '))
        numero2 = int(input('Ingresa el segundo número a multiplicar: '))
        resultado = numero1 * numero2
        print(f'El resultado de la multiplicación de los números {numero1} y {numero2} es: {resultado}')
    #Opción 4: Dividir
    elif seleccion_usuario == '4':
        try:
            numero1 = int(input('Ingresa el primer número a dividir: '))
            numero2 = int(input('Ingresa el segundo número a dividir: '))
            resultado = numero1 / numero2
        except ZeroDivisionError:
            print('No se puede divir por 0. Intenta nuevamente.')
        else:
            print(f'El resultado de la división entre los números {numero1} y {numero2} es: {resultado}')
    elif seleccion_usuario == '5':
        print('Hasta luego!')
        break
    else:
        print('Por favor ingresa una opción válida.')