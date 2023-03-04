from guizero import App, Text, TextBox, PushButton, Picture
import matplotlib.pyplot as plt

def resolver_sistema():
    x1 = float(x1_input.value)
    y1 = float(y1_input.value)
    c1 = float(c1_input.value)
    x2 = float(x2_input.value)
    y2 = float(y2_input.value)
    c2 = float(c2_input.value)
    
    det = x1*y2 - x2*y1
    det_x = c1*y2 - c2*y1
    det_y = x1*c2 - x2*c1
    
    if det == 0:
        resultado_texto.value = "No hay solución única."
        return
    
    x = det_x / det
    y = det_y / det
    
    resultado_texto.value = f"La solución es: x = {x}, y = {y}"
    
    fig, ax = plt.subplots()
    ax.axhline(y=0, color='k')
    ax.axvline(x=0, color='k')
    
    # Graficar la ecuación 1
    x_vals = [i for i in range(-10, 11)]
    y_vals = [(c1 - x1*x) / y1 for x in x_vals]
    ax.plot(x_vals, y_vals, '-r', label=f"{x1}x + {y1}y = {c1}")
    
    # Graficar la ecuación 2
    y_vals = [(c2 - x2*x) / y2 for x in x_vals]
    ax.plot(x_vals, y_vals, '-b', label=f"{x2}x + {y2}y = {c2}")
    
    # Graficar la intersección
    ax.plot(x, y, 'ko', label='Intersección')
    ax.legend()
    
    plt.show()

def limpiar_entradas():
    x1_input.clear()
    y1_input.clear()
    c1_input.clear()
    x2_input.clear()
    y2_input.clear()
    c2_input.clear()
    resultado_texto.clear()

# Crear la interfaz gráfica
app = App(title="Sistema de ecuaciones 2x2", width=500, height=500)

x1_etiqueta = Text(app, text="x1 = ")
x1_input = TextBox(app, width=5)
y1_etiqueta = Text(app, text="y1 = ")
y1_input = TextBox(app, width=5)
c1_etiqueta = Text(app, text="c1 = ")
c1_input = TextBox(app, width=5)

x2_etiqueta = Text(app, text="x2 = ")
x2_input = TextBox(app, width=5)
y2_etiqueta = Text(app, text="y2 = ")
y2_input = TextBox(app, width=5)
c2_etiqueta = Text(app, text="c2 = ")
c2_input = TextBox(app, width=5)

resultado_texto = Text(app, text="Ingrese los valores y haga clic en Calcular", size=14)

calcular_boton = PushButton(app, text="Calcular", command=resolver_sistema)
limpiar_boton = PushButton(app, text="Limpiar", command=limpiar_entradas)

app.display()

