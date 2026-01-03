# Calculadora com interfáz gráfica sencilla con TKinter
#
#
#
# Importación de tkinter y todos
# sus módulos necesarios para ejercicio
import tkinter as tk # Se importa la biblioteca principal de TKinter y dándole el alias 'tk'
from tkinter import ttk # Importa los widgets temáticos (para mejor apariencia)
from tkinter import messagebox # Para poder mostrar ventanas con diálogo

# Definición de la clase principal
class CalculadoraApp:
    # Método especial __init__: se ejecuta al CREAR una nueva instalcia de clase
    def __init__(self, root): # 'root' es la ventana principal que decibimos como parámetro
        self.root = root # Se guarda una referencia a la ventana principal en 'self.root'
        self.root.title('Calculadora Sencilla') # Establece el título de la ventana
        self.root.geometry('400x500') # Define el tamaño de la ventana (Ancho x alto)
        self.root.resizable(False, False) # Evita que el usuario pueda cambiar el tamaño

        # Variables especiales de Tkinter para almacenar valores de la interfaz
        self.numero1_var = tk.StringVar() # Variable que almacenará el primer número
        self.numero2_var = tk.StringVar() # Variable que almacenará el segundo número
        self.resultado_var = tk.StringVar(value='Resultado: ') # Variable que mostrará el resultado

        # Llamar a los métodos que configuran la aparienvia y crean la interfaz
        self.setup_estilos() # Configura colores, fuentes y estilos
        self.crear_interfaz() # Crea y organiza todos los elementos visuales 

    # Función para la definición de estilos
    def setup_estilos(self):
        # Configuración de los estilos visuales de la aplicación
        style = ttk.Style() # Se crea un objeto 'Style' para la apariencia
        style.theme_use('clam') # Aplica el tema 'clam' incorporado en Tkinter

    # Función para la mostrar la interfaz
    def crear_interfaz(self):
        # Crea todos los elementos de la interfaz gráfica
        
        # TÍTULO PRINCIPAL
        titulo = ttk.Label(self.root, # Crea una etiqueta en la ventana pricipal
                           text='Calculadora Sencilla', # Texto que se muestra
                           font=('Arial', 16, 'bold'))
        titulo.pack(pady=20) # Etiqueta de ventana con 20px de espacio vertical

def main():
    # Función principal para iniciar la aplicación
    root = tk.Tk()
    app = CalculadoraApp(root)
    root.mainloop()

if __name__ == '__main__':
    main()