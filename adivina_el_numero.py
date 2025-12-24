# Adivinar el número
#
#
#
#
# Importación del módulo random
import random

numero_usuario = int(input('Adivina el número entre el 1 y 100: '))
numero_aleatorio = random.randint(0, 100)

if numero_usuario == numero_aleatorio:
    print('Felicidades, le haz atinado!')
else:
    print(f'Lo siento, no adivinaste!. El número aleatorio era: {numero_aleatorio}')