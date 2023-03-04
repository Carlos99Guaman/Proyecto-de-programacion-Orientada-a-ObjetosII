import subprocess
import tkinter as tk

# Funciones para abrir los programas
def abrir_programa_1():
    subprocess.Popen(['python', 'Temperaturas.py'])

def abrir_programa_2():
    subprocess.Popen(['python', 'SisEcuaciones.py'])

def abrir_programa_3():
    subprocess.Popen(['python', 'JuegoSerpiente.py'])

def abrir_programa_4():
    subprocess.Popen(['python', 'programa4.py'])

# Configuración de la ventana y los botones
root = tk.Tk()
root.title("Proyecto de POO")
root.geometry("500x400")
root.resizable(False, False)
root.configure(bg="#f0f0f0")

label_titulo = tk.Label(root, text="Proyecto de POO", font=("Algerian", 20), bg="#f0f0f0")
label_titulo.pack(pady=10)

btn1 = tk.Button(root, text="Conversor de Temperatura", command=abrir_programa_1, font=("Arial", 12), bg="#4CAF50", fg="white")
btn1.pack(pady=10, padx=50)

btn2 = tk.Button(root, text="Sistema de Ecuaciones", command=abrir_programa_2, font=("Arial", 12), bg="#2196F3", fg="white")
btn2.pack(pady=10, padx=50)

btn3 = tk.Button(root, text="Juego de Serpiente", command=abrir_programa_3, font=("Arial", 12), bg="#FFC107", fg="white")
btn3.pack(pady=10, padx=50)

btn4 = tk.Button(root, text="Boton de prueba", command=abrir_programa_4, font=("Arial", 12), bg="#f44336", fg="white")
btn4.pack(pady=10, padx=50)

root.mainloop()
