from tkinter import *

def convertir_temp():
    temp = float(caja_temperatura.get())
    unidad_origen = menu_unidades_origen.get()
    unidad_destino = menu_unidades_destino.get()

    if unidad_origen == "Celsius":
        if unidad_destino == "Kelvin":
            temp_convertida = temp + 273.15
        elif unidad_destino == "Fahrenheit":
            temp_convertida = (temp * 9/5) + 32
        else:
            temp_convertida = temp
    elif unidad_origen == "Kelvin":
        if unidad_destino == "Celsius":
            temp_convertida = temp - 273.15
        elif unidad_destino == "Fahrenheit":
            temp_convertida = (temp - 273.15) * 9/5 + 32
        else:
            temp_convertida = temp
    else: # unidad_origen == "Fahrenheit"
        if unidad_destino == "Celsius":
            temp_convertida = (temp - 32) * 5/9
        elif unidad_destino == "Kelvin":
            temp_convertida = (temp - 32) * 5/9 + 273.15
        else:
            temp_convertida = temp

    caja_temperatura_convertida.delete(0, END)
    caja_temperatura_convertida.insert(0, temp_convertida)

ventana = Tk()
ventana.title("Conversor de temperatura")

frame_unidades = Frame(ventana)
frame_unidades.pack()

label_unidad_origen = Label(frame_unidades, text="Unidad de origen:")
label_unidad_origen.pack(side=LEFT)

menu_unidades_origen = StringVar(frame_unidades)
menu_unidades_origen.set("Celsius")

opcion_unidad_origen = OptionMenu(frame_unidades, menu_unidades_origen, "Celsius", "Kelvin", "Fahrenheit")
opcion_unidad_origen.pack(side=LEFT)

label_unidad_destino = Label(frame_unidades, text="Unidad de destino:")
label_unidad_destino.pack(side=LEFT)

menu_unidades_destino = StringVar(frame_unidades)
menu_unidades_destino.set("Celsius")

opcion_unidad_destino = OptionMenu(frame_unidades, menu_unidades_destino, "Celsius", "Kelvin", "Fahrenheit")
opcion_unidad_destino.pack(side=LEFT)

frame_temperatura = Frame(ventana)
frame_temperatura.pack()

label_temperatura = Label(frame_temperatura, text="Temperatura:")
label_temperatura.pack(side=LEFT)

caja_temperatura = Entry(frame_temperatura)
caja_temperatura.pack(side=LEFT)

label_temperatura_convertida = Label(frame_temperatura, text="Temperatura convertida:")
label_temperatura_convertida.pack(side=LEFT)

caja_temperatura_convertida = Entry(frame_temperatura)
caja_temperatura_convertida.pack(side=LEFT)

boton_convertir = Button(ventana, text="Convertir", command=convertir_temp)
boton_convertir.pack()

ventana.mainloop()
