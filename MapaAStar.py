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


def BuscarAStar(grafo, heuristica, nombreInicio, nombreFin):
    # Lista de los nodos evaludados
    nodosAbiertos = []
    nodosCerrados = []

    nodoInicio = Nodo(nombreInicio, None)
    nodoMeta = Nodo(nombreFin, None)

    # Se agrega nodo de incio a los abiertos
    nodosAbiertos.append(nodoInicio)

    # Evalua todos los nodos abiertos
    while (len(nodosAbiertos) > 0):
        # Ordena los nodos abiertos para tener el costo mas bajo de primero
        nodosAbiertos.sort()

        # Obtiene el nodo con menor costo
        nodoActual = nodosAbiertos.pop(0)

        # Agrega el nodo por evaluar a los cerrados
        nodosCerrados.append(nodoActual)

        # Se verifica si ya se llego al nodo buscado
        if (nodoActual == nodoMeta):
            path = []
            total = nodoActual.f
            while (nodoActual != nodoInicio):
                # path.append(nodoActual.nombre + ':' + str(nodoActual.g))
                path.append([nodoActual.nombre, nodoActual.f])
                nodoActual = nodoActual.padre

            # path.append(nodoInicio.nombre + ':' + str(nodoInicio.g))
            path.append([nodoInicio.nombre, nodoInicio.f])
            path.append(["Total:", total])

            # Se retorna la ruta (inicio > fin)
            return path[::-1]

        # Se obtinene vecinos
        nodosVecinos = grafo.Obtener(nodoActual.nombre)

        # Se evaluan los nodos vecinos
        for key, value in nodosVecinos.items():
            nodoVecino = Nodo(key, nodoActual)

            # Se verifica si ya el nodo fue evaluado
            if (nodoVecino in nodosCerrados):
                continue

            # Costo total f(n) = g(n) + h(n)
            # [DISTANCIA, ESTADO CARRETERA, PELIGROSIDAD]
            distancia = grafo.Obtener(nodoActual.nombre, nodoVecino.nombre)[0]
            estadoCarretera = grafo.Obtener(
                nodoActual.nombre, nodoVecino.nombre)[1]
            peligrosidad = grafo.Obtener(
                nodoActual.nombre, nodoVecino.nombre)[2]

            nodoVecino.g = nodoActual.g + distancia
            # nodoVecino.h = heuristica.get(nodoVecino.nombre)
            nodoVecino.h = abs(cost(distancia, estadoCarretera, peligrosidad))
            nodoVecino.f = nodoVecino.g + nodoVecino.h

            # Se verifica si el nodo vecino esta en nodos abierto y si tiene valor menor
            if (AgregarAbiertos(nodosAbiertos, nodoVecino) == True):
                # Si es mejor nodo, se agrega a los nodos por evaluar
                nodosAbiertos.append(nodoVecino)

    # Si no hay ruta
    return None

# Se verifica si el nodo vecino debe ser agregado a los nodos abiertos


def AgregarAbiertos(nodosAbiertos, nodoVecino):
    for nodo in nodosAbiertos:
        if (nodoVecino == nodo and nodoVecino.f > nodo.f):
            return False

    return True

# Definición de la función de costo


def cost(distancia, calle, peligrosidad):
    ip = (peligrosidad - 1)/4
    iec = (10 - calle)/9
    igc = 2*ip/3 + iec/3
    cn = int(distancia * (igc + 1))
    print(cn)
    return cn

# Definición de la función de costo (alternativa 1)


def cost2(distancia, calle, peligrosidad):
    return int(distancia * (2*(peligrosidad/5)/3 - (calle/10)/3))

# Definición de la función de costo (alternativa 2)


def cost3(distancia, calle, peligrosidad):
    return int(distancia * ((distancia/400)/4 + 2*(peligrosidad/5)/4 - (calle/10)/4))


def main():
    # Se creaa grafo no dirigido (misma distancia entre conexion de nodos)
    grafo = Grafo(dirigido=False)

    # Se crean las conexiones de los nodos [DISTANCIA, ESTADO CARRETERA, PELIGROSIDAD]
    grafo.CrearArista("Oradea", "Sibiu", [151, 6, 3])
    grafo.CrearArista("Oradea", "Zerind", [71, 6, 4])

    grafo.CrearArista("Zerind", "Arad", [75, 6, 5])

    grafo.CrearArista("Arad", "Sibiu", [140, 5, 4])
    grafo.CrearArista("Arad", "Timisoara", [118, 5, 3])

    grafo.CrearArista("Timisoara", "Lugoj", [111, 6, 3])
    grafo.CrearArista("Lugoj", "Mehadia", [70, 4, 4])
    grafo.CrearArista("Mehadia", "Dobreta", [75, 4, 3])

    grafo.CrearArista("Dobreta", "Craiova", [120, 7, 3])

    grafo.CrearArista("Craiova", "Rimnicu Vilcea", [146, 8, 1])
    grafo.CrearArista("Craiova", "Pitesti", [138, 6, 4])

    grafo.CrearArista("Pitesti", "Rimnicu Vilcea", [97, 7, 2])

    grafo.CrearArista("Sibiu", "Fagaras", [99, 7, 2])
    grafo.CrearArista("Sibiu", "Rimnicu Vilcea", [80, 6, 2])

    grafo.CrearArista("Neamt", "Iasi", [87, 5, 3])
    grafo.CrearArista("Iasi", "Vaslui", [92, 7, 4])
    grafo.CrearArista("Vaslui", "Urziceni", [142, 5, 2])
    grafo.CrearArista("Urziceni", "Hirsova", [98, 7, 4])
    grafo.CrearArista("Hirsova", "Eforie", [86, 7, 3])

    grafo.CrearArista("Pitesti", "Bucharest", [101, 8, 1])
    grafo.CrearArista("Fagaras", "Bucharest", [211, 8, 3])
    grafo.CrearArista("Urziceni", "Bucharest", [85, 9, 2])
    grafo.CrearArista("Giorgiu", "Bucharest", [90, 8, 1])

    # Heuristica de la distancia en linea recta
    distLineaRecta = {}

    # Lineas rectas de Rumania, hacia Bucharest
    distLineaRecta["Arad"] = 366
    distLineaRecta["Bucharest"] = 0
    distLineaRecta["Craiova"] = 160
    distLineaRecta["Dobreta"] = 242
    distLineaRecta["Eforie"] = 161
    distLineaRecta["Fagaras"] = 176
    distLineaRecta["Giorgiu"] = 77
    distLineaRecta["Hirsova"] = 151
    distLineaRecta["Iasi"] = 226
    distLineaRecta["Lugoj"] = 244
    distLineaRecta["Mehadia"] = 241
    distLineaRecta["Neamt"] = 234
    distLineaRecta["Oradea"] = 380
    distLineaRecta["Pitesti"] = 100
    distLineaRecta["Rimnicu Vilcea"] = 193
    distLineaRecta["Sibiu"] = 253
    distLineaRecta["Timisoara"] = 329
    distLineaRecta["Urziceni"] = 80
    distLineaRecta["Vaslui"] = 199
    distLineaRecta["Zerind"] = 374

    path = BuscarAStar(grafo, distLineaRecta, "Mehadia", "Bucharest")
    if (path != None):
        temp = "\nInicio > "
        total = path[0]
        for i in range(1, len(path)):
            temp += f'{path[i][0]} ({path[i][1]} km) > '

        temp += f'Meta\nTotal > {total[1]} km\n'
        print(temp)

    else:
        print("No hay ruta disponible")


main()
