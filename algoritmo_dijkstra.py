import sys

class Grafo:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.grafo = [[0 for _ in range(num_vertices)] for _ in range(num_vertices)]

    def encontrar_distancia_minima(self, distancias, visitado):
        min_distancia = sys.maxsize
        min_indice = -1

        for v in range(self.num_vertices):
            if distancias[v] < min_distancia and not visitado[v]:
                min_distancia = distancias[v]
                min_indice = v

        return min_indice

    def imprimir_ruta(self, padre, destino):
        if padre[destino] == -1:
            print(destino, end=' ')
            return
        self.imprimir_ruta(padre, padre[destino])
        print(destino, end=' ')

    def dijkstra(self, origen):
        distancias = [sys.maxsize] * self.num_vertices
        distancias[origen] = 0
        visitado = [False] * self.num_vertices
        padre = [-1] * self.num_vertices

        for _ in range(self.num_vertices):
            u = self.encontrar_distancia_minima(distancias, visitado)
            visitado[u] = True

            for v in range(self.num_vertices):
                if (
                    self.grafo[u][v] > 0 and
                    not visitado[v] and
                    distancias[v] > distancias[u] + self.grafo[u][v]
                ):
                    distancias[v] = distancias[u] + self.grafo[u][v]
                    padre[v] = u

        print("Nodo\tDistancia\tRuta")
        for nodo in range(self.num_vertices):
            print(f"{nodo}\t{distancias[nodo]}\t\t", end='')
            self.imprimir_ruta(padre, nodo)
            print()

# Ejemplo de uso
grafo = Grafo(9)
grafo.grafo = [
    [0, 4, 0, 0, 0, 0, 0, 8, 0],
    [4, 0, 8, 0, 0, 0, 0, 11, 0],
    [0, 8, 0, 7, 0, 4, 0, 0, 2],
    [0, 0, 7, 0, 9, 14, 0, 0, 0],
    [0, 0, 0, 9, 0, 10, 0, 0, 0],
    [0, 0, 4, 0, 10, 0, 2, 0, 0],
    [0, 0, 0, 14, 0, 2, 0, 1, 6],
    [8, 11, 0, 0, 0, 0, 1, 0, 7],
    [0, 0, 2, 0, 0, 0, 6, 7, 0]
]
grafo.dijkstra(0)
