# Calculadora sencilla reformulada
#
#
#
#
# La calculadora será reformulada a 
# base de funciones para su fácil mantenimiento
# y en caso de que se deseen agregar más funcionalidades

# Función para obtener los números ingresados por el usuario
def obtener_numeros():
    try:
        numero1 = int(input('Ingresa el primer número para la operación: '))
        numero2 = int(input('Ingresa el segundo número para la operación: '))
        return numero1, numero2
    except ValueError:
        print('Ingresa valores válidos por favor')
        return None, None
    
# Funciones para las funciones aritméticas
#
# Sumar
def sumar(numero1, numero2):
    return numero1 + numero2

# Restar
def restar(numero1, numero2):
    return numero1 - numero2

# Multiplicar
def multiplicar(numero1, numero2):
    return numero1 * numero2

# Dividir
def dividir(numero1, numero2):
    if numero2 == 0:
        raise ZeroDivisionError
    return numero1 / numero2

# Función principal que contiene menú y código principal
def main():
    while True:
        print('=' * 30)
        print('Puedes hacer las siguientes operaciones dentro de la calculadura:')
        print('1. Sumar')
        print('2. Restar')
        print('3. Multiplicar')
        print('4. Dividir')
        print('5. Salir')
        seleccion_usuario = input('Ingresa la opción que deseas hacer: ')
        print('=' * 30)

        # Si el usuario selecciona la acción 5 se cierra el bucle
        if seleccion_usuario == '5':
            print('Hasta luego!')
            break

        # Recepción de los números ingresados por el usuario en la función: def obtener_numeros():
        numero1, numero2 = obtener_numeros()
        # En caso de que el usuario no ingrese nada y de a enter
        if numero1 is None and numero2 is None:
            print('Por favor, ingresa algo.')
            continue

        # Conversión del menú de selección en un diccionario con llaves llamando a sus respectivas funciones aritméticas
        operaciones = {
            '1': sumar,
            '2': restar,
            '3': multiplicar,
            '4': dividir
        }

        # Inicialización de las operaciones
        if seleccion_usuario in operaciones:
            try:
                resultado = operaciones[seleccion_usuario](numero1, numero2)
                print(f'El resultado de la operación es: {resultado}')
            except ZeroDivisionError:
                print('No se puede divir por 0, por favor inténtalo nuevamente.')
        else:
            print('Ingresa algo válido.')

if __name__ == '__main__':
    main()