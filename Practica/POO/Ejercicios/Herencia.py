class Persona:
    def __init__(self,nombre:str,edad:int,nacionalidad:str):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad

class Empleado(Persona):
    def __init__(self,nombre:str,edad:int,nacionalidad:str,cargo:str,salario:float):
        super().__init__(nombre,edad,nacionalidad)
        self.cargo = cargo
        self.salario = salario

Roberto = Empleado("Roberto",23,"Colombia","Programador", 10232.99)

print(f"""
Datos del empleado:
Nombre: {Roberto.nombre}
Edad: {Roberto.edad}
Nacionalidad: {Roberto.nacionalidad}
Cargo: {Roberto.cargo}
Salario: {Roberto.salario}
""")