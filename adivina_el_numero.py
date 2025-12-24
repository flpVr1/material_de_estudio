# Adivinar el número
#
#
#
#
# Importación del módulo random
import random

numero_aleatorio = random.randint(1, 50)

# Mejora del código sin que se rompa apenas se pone un número y se mantenga el número aleatorio original sin que se reinicie solo
while True:
    numero_usuario = int(input('Intenta adivinar el número entre 1 y 50: '))

    if numero_usuario > numero_aleatorio:
        print('Lo siento, el número ingresado es muy alto. Intenta nuevamente')
    elif numero_usuario < numero_aleatorio:
        print('Lo siento, el número ingresado es muy bajo. Intenta nuevamente')
    else:
        print(f'Perfecto! Haz adivinado el número aleatorio {numero_aleatorio}')
        break