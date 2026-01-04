# Calculadora com interfáz gráfica sencilla con TKinter
#
#
#
# Importación de tkinter y todos
# sus módulos necesarios para ejercicio
import tkinter as tk # Se importa la biblioteca principal de TKinter y dándole el alias 'tk'
from tkinter import ttk # Importa los widgets temáticos (para mejor apariencia)
from tkinter import messagebox # Para poder mostrar ventanas con diálogo

######## 1. DEFINICIÓN DE LA CLASE PRINCIPAL ########
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

    ######## 2. FUNCIÓN PARA LA CONFIGURACIÓN DE LOS ESTILOS ########
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

    ######## 3. FUNCIÓN PARA LA CREACIÓN DE LA INTERFAZ GRÁFICA ########
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
        
        ######## 4. FRAMES para botones de operaciones ########
        frame_botones = ttk.Frame(self.root)
        frame_botones.pack(pady=30) # 30px de espacio vertical

        # LISTA con información de cada botón:
        # (texto, función a ejecutar, color de fondo)
        botones_operaciones = [
            ("➕ Sumar", self.sumar, '#4CAF50'),  # Botón verde
            ("➖ Restar", self.restar, '#2196F3'),  # Botón azul
            ("✖ Multiplicar", self.multiplicar, '#FF9800'),  # Botón naranja
            ("➗ Dividir", self.dividir, '#F44336'),  # Botón rojo
        ]

        # BUCLE para mostrar los 4 botones
        for i, (texto, comando, color) in enumerate(botones_operaciones):
            # NOTA: Se está usando tk.Button en lugar de ttk.Button para tener más control visual
            btn = tk.Button(frame_botones, # Crea el botón en el frame_botones
                            text=texto, # Texto con emoji y nombre
                            command=comando, # Función a ejecutar el click
                            bg=color, # Color de fondo
                            fg='white', # Color del texto (foreground)
                            font=('Arian', 10, 'bold',), # Fuente
                            relief='raised', # Efecto 3D 'Elevado'
                            width=15, # Ancho en caracteres
                            height=2, # Alto en líneas de texto
                            cursor='hand2') # Cambia el cursor a una mano si pasa sobre el botón
            
            # Organizar botones en grid de 2x2
            btn.grid(row=i//2, # Fila: 0, 0, 1, 1 (división entera)
                    column=i%2, # Columna: 0, 1, 0, 1 (módulo)
                    padx=10, # 10px espacio horizontal entre botones
                    pady=10) # 10px espacio vertical entre botones
            
            # Eventos para el efecto visual al pasar el mouse
            btn.bind('<Enter>', # Cuando el mouse ENTRA en el botón
                    lambda e, b=btn: b.config(relief='sunken')) # Vuelve a efecto de 'Elevado'
            btn.bind('<Leave>',
                    lambda e, b=btn: b.config(relief='raised'))
            
        ######## 5. ÁREA DE RESULTADOS ########
        #
        # Frame para mostrar el resultado
        frame_resultado = ttk.Frame(self.root,
                                    relief='solid',
                                    borderwidth=1)
        frame_resultado.pack(pady=20,
                             padx=20,
                             fill='x')
        
        # Etiqueta de "Resultado"
        ttk.Label(frame_resultado, text='RESULTADO: ',
                  font=('Arial', 11, 'bold')).pack(pady=(10, 5))
        
        # Etiqueta donde aparecerá el resultado (vinculada a resultado_var)
        resultado_label = ttk.Label(frame_resultado,
                                    textvariable=self.resultado_var,
                                    font=('Arial', 14, 'bold'),
                                    foreground='#2E7D32')
        
        resultado_label.pack(pady=(5, 15))

        ######## 6. BOTONES DE CONTROL ########
        #
        # Botón "Limpiar"
        ttk.Button(self.root,
                   text='Limpiar',
                   command=self.limpiar,
                   style='TButton').pack(pady=10)
        
        # Botón "Salir"
        ttk.Button(self.root,
                   text='Salir',
                   command=self.root.quit,
                   style='TButton').pack(pady=10)
            
    # MÉTODOS DE FUNCIONALIDAD
    #
    # Ontención de los números ingresados por el usuario
    def obtener_numeros(self):
        try:
            # .get() obtiene el texto de las variables StringVar # Lineas 21 - 22 - 23
            # .strip() elimina espacios al inicio y al final
            num1 = float(self.numero1_var.get().strip())
            num2 = float(self.numero2_var.get().strip())
            return num1, num2 # Devuelve los valores si son válidos
        except ValueError:
            messagebox.showerror('Error de entrada',
                                'Por favor ingresa números válidos.')
            return None, None # Devuelve valores nulos
    
    # FUNCIONES ARITMÉTICAS
    #
    # SUMA
    def sumar(self):
        num1, num2 = self.obtener_numeros() # Obtener números validados
        if num1 is not None and num2 is not None: # Si son válidos
            resultado = num1 + num2 # Realiza la suma
            self.mostrar_resultado(f'El resultado entre {num1} y {num2} es: {resultado}')

    # RESTA
    def restar(self):
        num1, num2 = self.obtener_numeros()
        if num1 is not None and num2 is not None:
            resultado = num1 - num2
            self.mostrar_resultado(f'El resultado entre {num1} y {num2} es: {resultado}')
    
    # MULTIPLICACIÓN
    def multiplicar(self):
        num1, num2 = self.obtener_numeros()
        if num1 is not None and num2 is not None:
            resultado = num1 * num2
            self.mostrar_resultado(f'El resultado entre {num1} y {num2} es: {resultado}')

    # DIVISIÓN
    def dividir(self):
        num1, num2 = self.obtener_numeros()
        if num1 is not None and num2 is not None:
            if num2 == 0: # Validación de división por cero
                messagebox.showerror('Error matemático',
                                    'No se puede dividir por 0.')
                return # Sale sin hacer la operación
            resultado = num1 / num2
            self.mostrar_resultado(f'el resultado entre {num1} y {num2} es: {resultado}')

    # MÉTODOS AUXILIARES
    #
    # Función para mostrar el resultado
    def mostrar_resultado(self, texto):
        self.resultado_var.set(texto)

    # Función para limpiar la pantalla
    def limpiar(self):
        # Limpieaz de todos los campos
        self.numero1_var.set('')
        self.numero2_var.set('')
        self.resultado_var.set('Resultado: ') # Restablece el mensaje inicial

        # Regresa el foco al primer campo
        self.root.focus_set()
        # Buscando el primer campo Entry y le da el foco
        for widget in self.root.winfo_children(): # Recorre todos los widget hijos
            if isinstance(widget, ttk.Entry): # Si es un campo de entrada
                widget.focus() # Le da el foco
                break

def main():
    # Función principal para iniciar la aplicación
    root = tk.Tk()
    app = CalculadoraApp(root)
    root.mainloop()

if __name__ == '__main__':
    main()