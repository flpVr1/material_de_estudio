# Lista de nombres ingresadas por el usuario
#
#
#
#
nombres = []

for i in range(5):
    nombre = input(f'Ingresa un nombre: {i + 1}. ')
    nombres.append(nombre)

print(nombres)