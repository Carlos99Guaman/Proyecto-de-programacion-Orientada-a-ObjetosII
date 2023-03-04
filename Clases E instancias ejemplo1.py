#Definicion de una clase en python
class Auto:
    #Atributos de la clase Auto
    marca=" Ford ";
    año=2023;
    #constructor de mi clase persona
    def __init__(self,transmision,telefono):
        self.transmision=transmision
        
        #Metodo notasPersona
    def Cfuerza(self,nota):
        print(" Caballos de fuerza del Auto  ",nota)

#Instancia de la clase persona
p=Auto(" Automática",400) 

print(" Marca del Auto ",p.marca)
print(" La Transmision del Auto es ",p.transmision)
p.Cfuerza(400)

