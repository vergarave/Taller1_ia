from typing import Any, Tuple
from algorithms import utils
from algorithms.problems import MultiSurvivorProblem
import math


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def manhattanHeuristic(state, problem):
    """
    The Manhattan distance heuristic.
    """
    # TODO: Add your code here
    x, y = state
    xg, yg = problem.goal
    return abs(xg - x) + abs(yg - y)


def euclideanHeuristic(state, problem):
    """
    The Euclidean distance heuristic.
    """
    # TODO: Add your code here
    x, y = state
    xg, yg = problem.goal
    return math.sqrt((xg - x) ** 2 + (yg - y) ** 2)

#Si hay más de un sobreviviente como dice se puede usar la distancia 
# al sobreviviente más cercano y sumarle el costo del MST sobre los 
# sobrevivientes que quedan

#Es por esto que se crea primero la función mst_cost_prim que calcula 
# el costo del MST usando el algoritmo de Prim. 

def manhattanDistance(inicio, fin):
    """
    Recibe dos puntos cualquiera y calcula la distancia entre ellos 
    usando la distancia Manhattan.
    """
    return abs(fin[0] - inicio[0]) + abs(fin[1] - inicio[1])

def mst_cost_prim(nodos):
    # VERSIÓN INICIAL:
    # Recorría todos los nodos no visitados para encontrar el más cercano,
    # pero comparaba cada nodo v solo contra el último agregado al árbol
    # en lugar de contra todos los nodos ya en el árbol. 
    #
    # n = len(nodos)
    # if n <= 1:
    #     return 0
    # visitados = {nodos[0]}
    # costo_total = 0
    # while len(visitados) < n:
    #     ultimo = list(visitados)[-1]
    #     mejor_costo = float("inf")
    #     mejor_nodo = None
    #     for v in nodos:
    #         if v not in visitados:
    #             c = manhattanDistance(ultimo, v)
    #             if c < mejor_costo:
    #                 mejor_costo = c
    #                 mejor_nodo = v
    #     visitados.add(mejor_nodo)
    #     costo_total += mejor_costo
    #
    # PROMPT:
    # "Esta función no está encontrando el MST correcto en todos los casos,
    #  ayudame a corregirla"
    #
    # CORRECCIÓN::
    # El error era comparar solo contra el último nodo agregado. Prim requiere
    # buscar la arista mínima desde CUALQUIER nodo ya en el árbol hacia
    # cualquier nodo fuera. 
    
    n = len(nodos)
    if n <= 1:
        return 0

    visitados = {nodos[0]}
    costo_total = 0

    while len(visitados) < n:
        mejor_costo = float("inf")
        mejor_nodo = None
         # Correcion de Claude
        for u in visitados:         
            for v in nodos:
                if v not in visitados:
                    c = manhattanDistance(u, v)
                    if c < mejor_costo:
                        mejor_costo = c
                        mejor_nodo = v
        visitados.add(mejor_nodo)
        costo_total += mejor_costo

    return costo_total
    
    n = len(nodos)
    if n <= 1:
        return 0
    
    visitados = {nodos[0]}
    costo_total = 0

    while len(visitados) < n:
        mejor_costo = float("inf")
        mejor_nodo = None
        for u in visitados:
            for v in nodos:
                if v not in visitados:
                    c = manhattanDistance(u, v)
                    if c < mejor_costo:
                        mejor_costo = c
                        mejor_nodo = v
        visitados.add(mejor_nodo)
        costo_total += mejor_costo

    return costo_total


def survivorHeuristic(state: Tuple[Tuple, Any], problem: MultiSurvivorProblem):
    """
    Your heuristic for the MultiSurvivorProblem.

    state: (position, survivors_grid)
    problem: MultiSurvivorProblem instance

    This must be admissible and preferably consistent.

    Hints:
    - Use problem.heuristicInfo to cache expensive computations
    - Go with some simple heuristics first, then build up to more complex ones
    - Consider: distance to nearest survivor + MST of remaining survivors
    - Balance heuristic strength vs. computation time (do experiments!)
    """
    
    # VERSIÓN INICIAL:
    # Solo devolvía la distancia al sobreviviente más cercano,
    # sin considerar el MST para los restantes.
    #
    # position, survivors_grid = state
    # survivors_list = survivors_grid.asList()
    # if len(survivors_list) == 0:
    #     return 0
    # min_distance = float('inf')
    # for survivor_pos in survivors_list:
    #     distance = manhattanDistance(position, survivor_pos)
    #     if distance < min_distance:
    #         min_distance = distance
    # return min_distance
    #
    # PROMPT usado con Claude:
    # "Ayudame a corregir esta funcion, ten en cuenta los Hints que da
    #  la descripcion de la funcion"
    #
    # CORRECCIÓN:
    # La versión inicial era admisible pero no estimaba el costo
    # de visitar a los sobrevivientes que quedan después del primero.
    # Claude nos ayudo a agregar el MST sobre los sobrevivientes que quedaban
    # y usar problem.heuristicInfo para no recalcularlo cada vez.
    
    position, survivors_grid = state
    survivors_list = survivors_grid.asList()
    
    if len(survivors_list) == 0:
        return 0
    
    # Distancia al sobreviviente más cercano
    min_distance = float('inf')
    for survivor_pos in survivors_list:
        distance = manhattanDistance(position, survivor_pos)
        if distance < min_distance:
            min_distance = distance
        
    # Si hay solo un sobreviviente, la heurística es la distancia a ese sobreviviente
    if len(survivors_list) == 1:
        return min_distance
    
    # MST sobre los sobrevivientes restantes
    survivors_key = tuple(sorted(survivors_list))
    
    if survivors_key not in problem.heuristicInfo:
        problem.heuristicInfo[survivors_key] = mst_cost_prim(survivors_list)

    return min_distance + problem.heuristicInfo[survivors_key]