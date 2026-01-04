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

        # Configuración del color de fondo
        self.root.configure(bg='#f0f0f0')

        # Configuración de estilos para diferentes tipos de widgets
        style.configure('TLabel', # Estilo para todas las etiquetas (label)
                        background="#f0f0f0",
                        font=('Arial', 10))
        
        style.configure('TButton', # Estilo para todos los botones
                        font=('Arial', 10, 'bold'),
                        padding=10)
        
        style.configure('TEntry', # Estilo para campos de entrada 'Entry'
                        font=('Arial', 11),
                        padding=5)
        
        # Configuración de colores DÍNAMICOS para botones (cambian al pasar el mouse)
        style.map('TButton',
                background=[('active', '#4CAF50'),
                            ('!active', '#5cb85c')],
                foreground=[('active', 'white'),
                            ('!active', 'white')])

    # Función para la mostrar la interfaz
    def crear_interfaz(self):
        # Crea todos los elementos de la interfaz gráfica
        
        # TÍTULO PRINCIPAL
        titulo = ttk.Label(self.root, # Crea una etiqueta en la ventana pricipal
                           text='Calculadora Sencilla', # Texto que se muestra
                           font=('Arial', 16, 'bold'))
        titulo.pack(pady=20) # Etiqueta de ventana con 20px de espacio vertical

        # Frame para campos de entrada (Frame es un contenedor para organizar widgets)
        frame_entradas = ttk.Frame(self.root, #Crea un frame dentro de la ventana
                                  padding=15) # 15px de espacio interno en todos los lados
        
        frame_entradas.pack(fill='x', # Coloca el Frame expandiéndolo horizontalmente
                            padx=20) #20 px de espacio horizontal externo
        
        # Primer Número
        ttk.Label(frame_entradas, # Creación de una etiqueta DENTRO del Frame
                  text='Primer número: ').grid( # grid() organiza en filas y columnas
                      row=0, # Fila 0 (Primera fila)
                      column=0, # Columna 0 (Primera columna)
                      sticky='w', # Alinea el texto a la izquierda (w de west)
                      pady=5 # 5px de espacio vertical
                  )
        
        entrada1 = ttk.Entry(frame_entradas, #Crea un campo de entrada de texto
                             textvariable=self.numero1_var, # Vincula con la variable que almacena su valor
                             font=('Arial', 11), # Fuente
                             width=25) # Su ancho en caracteres
        
        entrada1.grid(row=0, # Fila 0
                      column=1, # Columna 1 (Al lado de la etiqueta)
                      pady=5, # 5px de espacio vertical
                      padx=(10,0)) # 10px de espacio a la izquierda, 0 a la derecha 
        
        entrada1.focus()

        # Segundo Número
        ttk.Label(frame_entradas,
                  text='Segundo número: ').grid(
                    row=1,
                    column=0,
                    sticky='w',
                    pady=5
                  )
        
        entrada2 = ttk.Entry(frame_entradas,
                            textvariable=self.numero2_var,
                            font=('Arial', 11),
                            width=25)
        
        entrada2.grid(row=1,
                      column=1,
                      pady=5,
                      padx=(10,0))

def main():
    # Función principal para iniciar la aplicación
    root = tk.Tk()
    app = CalculadoraApp(root)
    root.mainloop()

if __name__ == '__main__':
    main()