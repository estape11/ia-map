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
					Programa Principal
*******************************************************************
"""

from Grafo import Grafo
from Nodo import Nodo

# Busqueda A*
def BuscarAStar(grafo, heuristica, start, end):
	# Lista de los nodos evaludados
	nodosAbiertos = []
	nodosCerrados = []

	nodoInicio = Nodo(start, None)
	nodoMeta = Nodo(end, None)

	# Se agrega nodo de incio a los abiertos
	nodosAbiertos.append(nodoInicio)

	# Evalua todos los nodos abiertos
	while ( len(nodosAbiertos) > 0 ):
		# Ordena los nodos abiertos para tener el costo mas bajo de primero
		nodosAbiertos.sort()

		# Obtiene el nodo con menor costo
		nodoActual = nodosAbiertos.pop(0)

		# Agrega el nodo por evaluar a los cerrados
		nodosCerrados.append(nodoActual)

		# Se verifica si ya se llego al nodo buscado
		if ( nodoActual == nodoMeta ):
			path = []
			while ( nodoActual != nodoInicio ):
				path.append(nodoActual.nombre + ':' + str(nodoActual.g))
				nodoActual = nodoActual.padre

			path.append(nodoInicio.nombre + ':' + str(nodoInicio.g))
			# Se retorna la ruta (inicio > fin)
			return path[::-1]

		# Se obtinene vecinos
		nodosVecinos = grafo.Obtener(nodoActual.nombre)

		# Se evaluan los nodos vecinos
		for key, value in nodosVecinos.items():
			nodoVecino = Nodo(key, nodoActual)

			# Se verifica si ya el nodo fue evaluado
			if ( nodoVecino in nodosCerrados ):
				continue

			# Costo total f(n) = g(n) + h(n)
			nodoVecino.g = nodoActual.g + grafo.Obtener(nodoActual.nombre, nodoVecino.nombre)[0]
			nodoVecino.h = heuristica.get(nodoVecino.nombre)
			nodoVecino.f = nodoVecino.g + nodoVecino.h

			# Se verifica si el nodo vecino esta en nodos abierto y si tiene valor menor
			if ( AgregarAbiertos(nodosAbiertos, nodoVecino) == True ):
				# Si es mejor nodo, se agrega a los nodos por evaluar
				nodosAbiertos.append(nodoVecino)

	# Si no hay ruta
	return None

# Se verifica si el nodo vecino debe ser agregado a los nodos abiertos
def AgregarAbiertos(nodosAbiertos, nodoVecino):
	for node in nodosAbiertos:
		if (nodoVecino == node and nodoVecino.f > node.f):
			return False

	return True

def main():
	# Se creaa grafo no dirigido (misma distancia entre conexion de nodos)
	grafo = Grafo(dirigido=False)

	# Se crean las conexiones de los nodos
	grafo.CrearArista('Frankfurt', 'Wurzburg', [111])
	grafo.CrearArista('Frankfurt', 'Mannheim', [85])
	grafo.CrearArista('Wurzburg', 'Nurnberg', [104])
	grafo.CrearArista('Wurzburg', 'Stuttgart', [140])
	grafo.CrearArista('Wurzburg', 'Ulm', [183])
	grafo.CrearArista('Mannheim', 'Nurnberg', [230])
	grafo.CrearArista('Mannheim', 'Karlsruhe', [67])
	grafo.CrearArista('Karlsruhe', 'Basel', [191])
	grafo.CrearArista('Karlsruhe', 'Stuttgart', [64])
	grafo.CrearArista('Nurnberg', 'Ulm', [171])
	grafo.CrearArista('Nurnberg', 'Munchen', [170])
	grafo.CrearArista('Nurnberg', 'Passau', [220])
	grafo.CrearArista('Stuttgart', 'Ulm', [107])
	grafo.CrearArista('Basel', 'Bern', [91])
	grafo.CrearArista('Basel', 'Zurich', [85])
	grafo.CrearArista('Bern', 'Zurich', [120])
	grafo.CrearArista('Zurich', 'Memmingen', [184])
	grafo.CrearArista('Memmingen', 'Ulm', [55])
	grafo.CrearArista('Memmingen', 'Munchen', [115])
	grafo.CrearArista('Munchen', 'Ulm', [123])
	grafo.CrearArista('Munchen', 'Passau', [189])
	grafo.CrearArista('Munchen', 'Rosenheim', [59])
	grafo.CrearArista('Rosenheim', 'Salzburg', [81])
	grafo.CrearArista('Passau', 'Linz', [102])
	grafo.CrearArista('Salzburg', 'Linz', [126])

	# Se hace el grafo no dirigido
	#grafo.HacerNoDirigido()

	# Heuristica de la distancia en linea recta
	distLineaRecta = {}
	distLineaRecta['Basel'] = 204
	distLineaRecta['Bern'] = 247
	distLineaRecta['Frankfurt'] = 215
	distLineaRecta['Karlsruhe'] = 137
	distLineaRecta['Linz'] = 318
	distLineaRecta['Mannheim'] = 164
	distLineaRecta['Munchen'] = 120
	distLineaRecta['Memmingen'] = 47
	distLineaRecta['Nurnberg'] = 132
	distLineaRecta['Passau'] = 257
	distLineaRecta['Rosenheim'] = 168
	distLineaRecta['Stuttgart'] = 75
	distLineaRecta['Salzburg'] = 236
	distLineaRecta['Wurzburg'] = 153
	distLineaRecta['Zurich'] = 157
	distLineaRecta['Ulm'] = 0

	path = BuscarAStar(grafo, distLineaRecta, 'Basel', 'Ulm')
	print(path)
	print()
	#print(grafo.grafoDict)

main()