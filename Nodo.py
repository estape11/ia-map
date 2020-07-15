#!/usr/bin/python3

"""
*******************************************************************
					Inteligencia Artificial
*******************************************************************
	Programador: Esteban Aguero Perez (estape11)
	Equipo: Esteban, Yenira, Eduardo
	Lenguaje: Python
	Version: 0.10
	Ultima Modificacion: 14/07/2020
	Descripcion:	
					Clase Nodo
*******************************************************************
"""

class Nodo:
	def __init__(self, nombre:str, padre:str):
		self.nombre = nombre
		self.padre = padre
		self.g = 0 # Distancia que lleva desde el nodo inicio
		self.h = 0 # Distancia hacia el nodo meta
		self.f = 0 # Costo total

	# Se hace override de los operadores basicos
	def __eq__(self, other):
		return self.nombre == other.nombre

	def __lt__(self, other):
		return self.f < other.f

	def __repr__(self):
		return ('({0},{1})'.format(self.position, self.f))