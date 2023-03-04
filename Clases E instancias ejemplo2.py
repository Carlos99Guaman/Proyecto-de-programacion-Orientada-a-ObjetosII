class Fruta:
    def __init__(self, nombre, color, sabor):
        self.nombre = nombre
        self.color = color
        self.sabor = sabor

    def describe(self):
        print(f"La {self.nombre} es de color {self.color} y tiene un sabor {self.sabor}.")
#En este ejemplo, estamos creando una clase llamada Fruta. La clase tiene un constructor (__init__) que toma tres parámetros (nombre, color y sabor) y define tres atributos (nombre, color y sabor). También tiene un método (describe) que imprime una descripción de la fruta utilizando los atributos nombre, color y sabor.

#Ahora, podemos crear instancias de la clase Fruta para representar diferentes tipos de frutas:


manzana = Fruta("manzana", "rojo", "dulce")
uva = Fruta("Uva", "morado o verde", "suave")
naranja = Fruta("naranja", "anaranjado", "ácido")

manzana.describe()  # La manzana es de color rojo y tiene un sabor dulce.
uva.describe()  # El plátano es de color amarillo y tiene un sabor suave.
naranja.describe()  # La naranja es de color anaranjado y tiene un sabor ácido.        