class Estudiante:
    def __init__(self, nombre, apellido, edad, semestre, promedio):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.semestre = semestre
        self.promedio = promedio

    def Estudiar(self):
        print(f'El/La estudiante {self.nombre + " " + self.apellido} esta estudiando')

nombre = input('Ingrese su nombre: ')
apellido = input('Ingrese su apellido: ')
edad = int(input('Ingrese su edad: '))
semestre = int(input('Ingrese su semestre: '))
promedio = float(input('Ingrese su promedio: '))

Estudiante = Estudiante(nombre, apellido, edad, semestre, promedio)

print(f"""
Datos del estudiante:\n
Estudiante -> :\n
Nombre: {Estudiante.nombre}
Apellido: {Estudiante.apellido}
Edad: {Estudiante.edad}
Semestre: {Estudiante.semestre}
Promedio: {Estudiante.promedio}
""")

estudiar = input()
Estudiante.Estudiar() if estudiar.lower() == 'Estudiar' or 'Estudio' else print('No se puede realizar la accion')
