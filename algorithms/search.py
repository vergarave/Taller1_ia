from algorithms.problems import SearchProblem
import algorithms.utils as utils
from world.game import Directions
from algorithms.heuristics import nullHeuristic


def tinyHouseSearch(problem: SearchProblem):
    """
    Returns a sequence of moves that solves tinyHouse. For any other building, the
    sequence of moves will be incorrect, so only use this for tinyHouse.
    """
    s = Directions.SOUTH
    w = Directions.WEST
    return [s, s, w, s, w, w, s, w]


def depthFirstSearch(problem: SearchProblem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
        # 1) Estructura LIFO para DFS
    frontier = utils.Stack()

    # 2) Estado inicial
    start_state = problem.getStartState()

    # Si ya estamos en la meta, no hacemos ningún movimiento
    if problem.isGoalState(start_state):
        return []

    # 3) Conjunto de visitados para evitar ciclos/repeticiones
    visited = set()
    visited.add(start_state)

    # Cada elemento de la frontera será: (estado_actual, lista_acciones_hasta_aca)
    frontier.push((start_state, []))

    # 4) Bucle principal de DFS
    while not frontier.isEmpty():
        state, actions = frontier.pop()

        # Si llegamos a la meta, devolvemos el plan (lista de movimientos)
        if problem.isGoalState(state):
            return actions

        # Expandimos sucesores: (nextState, action, stepCost)
        for next_state, action, step_cost in problem.getSuccessors(state):
            if next_state not in visited:
                visited.add(next_state)
                frontier.push((next_state, actions + [action]))

    # Si no hay solución (no debería pasar en mapas válidos), devolvemos vacío
    return []


def breadthFirstSearch(problem: SearchProblem):
    """
    Search the shallowest nodes in the search tree first.
    """
    # TODO: Add your code here
    utils.raiseNotDefined()


def uniformCostSearch(problem: SearchProblem):
    """
    Search the node of least total cost first.
    """

    # TODO: Add your code here
    utils.raiseNotDefined()


def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic):
    """
    Search the node that has the lowest combined cost and heuristic first.
    """
    # TODO: Add your code here
    utils.raiseNotDefined()


# Abbreviations (you can use them for the -f option in main.py)
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
