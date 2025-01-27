class Celular:
    def __init__(self, marca:str, modelo:str, camara:str, precio:float):
        self.marca = marca
        self.modelo = modelo
        self.camara = camara
        self.precio = precio
        
celular1 = Celular("Motorola","MotoG86","28MP",900000)
print(celular1.marca)
print(2+3*4)
print("Hello, World!"[7:])
my_list = [10, 20, 30, 40, 50]



del my_list[2]



print(my_list)