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
					Clase Grafo
*******************************************************************
"""

class Grafo:
	def __init__(self, grafoDict=None, dirigido=True):
		self.grafoDict = grafoDict or {}
		self.dirigido = dirigido
		if ( not dirigido ):
			self.HacerNoDirigido()

	# Hace que el peso de la arista sea bidireccional
	def HacerNoDirigido(self):
		for a in list(self.grafoDict.keys()):
			for (b, dist) in self.grafoDict[a].items():
				self.grafoDict.setdefault(b, {})[a] = dist

	# Crea una arista para conectar dos nodos
	def CrearArista(self, A, B, distance=1):
		self.grafoDict.setdefault(A, {})[B] = distance
		if ( not self.dirigido ):
			self.grafoDict.setdefault(B, {})[A] = distance

	# Obtiene nodos vecinos
	def Obtener(self, a, b=None):
		aristas = self.grafoDict.setdefault(a, {})
		if ( b is None ):
			return aristas

		else:
			return aristas.get(b)

	# Lista de nodos en el grafo
	def Nodos(self):
		s1 = set([k for k in self.grafoDict.keys()])
		s2 = set([k2 for v in self.grafoDict.values() for k2, v2 in v.items()])
		nodos = s1.union(s2)
		return list(nodos)