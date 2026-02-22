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
    lifo=utils.Stack()
    estado_inicial= problem.getStartState()

    if problem.isGoalState(estado_inicial):
        return []

    visited=set()
    visited.add(estado_inicial)
    lifo.push((estado_inicial, []))

    while not lifo.isEmpty():
        estado,actions = lifo.pop()
        if problem.isGoalState(estado):
            return actions

        for sig, action, cost in problem.getSuccessors(estado):
            if sig not in visited:
                visited.add(sig)
                lifo.push((sig,actions + [action]))
    
    return []


def breadthFirstSearch(problem: SearchProblem):
    """
    Search the shallowest nodes in the search tree first.
    """
    fifo=utils.Queue()
    estado_inicial= problem.getStartState()

    if problem.isGoalState(estado_inicial):
        return []

    visited=set()
    visited.add(estado_inicial)
    fifo.push((estado_inicial, []))

    while not fifo.isEmpty():
        estado,actions = fifo.pop()
        if problem.isGoalState(estado):
            return actions
    
        for sig, action, cost in problem.getSuccessors(estado):
            if sig not in visited:
                visited.add(sig)
                fifo.push((sig,actions + [action]))
    
    return []


def uniformCostSearch(problem: SearchProblem):
    """
    Search the node of least total cost first.
    """
    # VERSIÓN INICIAL:
    # El problema principal era que se llamaba problem.isGoalState() sin pasarle
    # ningún estado. Esta función no devuelve el estado objetivo, sino que recibe
    # un estado y retorna True/False indicando si se llegó al objetivo.
    # Además, la comparación estado_inicial == estado_final era redundante
    # y no estaba hecha correctamente.
    #
    # estado_inicial = problem.getStartState()
    # estado_final = problem.isGoalState()
    # pq = utils.PriorityQueue()
    # if estado_inicial == estado_final:
    #     return []
    # visited = set()
    # pq.push((estado_inicial, [], 0), 0)
    # while not pq.isEmpty():
    #     state, actions, cost = pq.pop()
    #     if problem.isGoalState(state):
    #         return actions
    #     for next_state, action, nextCost in problem.getSuccessors(state):
    #         new_cost = cost + nextCost
    #         pq.push((next_state, actions + [action], new_cost), new_cost)
    # return []
    #
    # PROMPT usado con Claude:
    # "Esta función tiene errores, ayudame a corregirla y optimizarla"
    #
    # CORRECCIÓN de la IA:
    # isGoalState no retorna el estado goal sino True/False dado un estado.
    # La verificación se hace con problem.isGoalState(estado_inicial).
    # Se agregó visited para evitar expandir el mismo nodo múltiples veces,
    # lo cual puede colgar el programa en mapas grandes con ciclos.

    pq = utils.PriorityQueue()
    estado_inicial = problem.getStartState()
    pq.push((estado_inicial, [], 0), 0)
    visited = set()

    while not pq.isEmpty():
        state, actions, costo = pq.pop()

        if state in visited:
            visited.add(state)

        if problem.isGoalState(state):
            return actions

        for next, action, nextCost in problem.getSuccessors(state):
            if next not in visited:
                newCost = costo + nextCost
                pq.push((next, actions + [action], newCost), newCost)

    return []

def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic):
    """
    Search the node that has the lowest combined cost and heuristic first.
    """
    pq = utils.PriorityQueue()
    start = problem.getStartState()
    
    pq.push((start, [], 0), heuristic(start, problem))
    
    best_g = {}
    
    while not pq.isEmpty():
        state, actions, g =pq.pop()
        if state not in best_g or best_g[state] > g:
            best_g[state] = g
            if problem.isGoalState(state):
                return actions
            for next_state, action, cost in problem.getSuccessors(state):
                new_g = g + cost
                f = new_g + heuristic(next_state, problem)
                pq.push((next_state, actions + [action], new_g), f)
    return []


# Abbreviations (you can use them for the -f option in main.py)
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
