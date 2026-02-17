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
