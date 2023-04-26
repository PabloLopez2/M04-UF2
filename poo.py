#!/usr/bin/python3

class Alumno:
	
	def __init__(self, nombre):
		self.name = nombre

	def saluda (self):
		print("ola k ase "+self.name)

if __name__ == "__main__":
	marti = Alumno("Martí")

	marti.saluda()
	
	alumnos = [Alumno("Lluc"), Alumno("Marcel"), Alumno("Pablo")]

	for alumno in alumnos:
		alumno.saluda()
	
	alumnos[0].saluda()
