# search.py
# ---------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html

"""
In search.py, you will implement generic search algorithms which are called 
by Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
  """
  This class outlines the structure of a search problem, but doesn't implement
  any of the methods (in object-oriented terminology: an abstract class).
  
  You do not need to change anything in this class, ever.
  """
  
  def getStartState(self):
     """
     Returns the start state for the search problem 
     """
     util.raiseNotDefined()
    
  def isGoalState(self, state):
     """
       state: Search state
    
     Returns True if and only if the state is a valid goal state
     """
     util.raiseNotDefined()

  def getSuccessors(self, state):
     """
       state: Search state
     
     For a given state, this should return a list of triples, 
     (successor, action, stepCost), where 'successor' is a 
     successor to the current state, 'action' is the action
     required to get there, and 'stepCost' is the incremental 
     cost of expanding to that successor
     """
     util.raiseNotDefined()

  def getCostOfActions(self, actions):
     """
      actions: A list of actions to take
 
     This method returns the total cost of a particular sequence of actions.  The sequence must
     be composed of legal moves
     """
     util.raiseNotDefined()
           

def tinyMazeSearch(problem):
  """
  Returns a sequence of moves that solves tinyMaze.  For any other
  maze, the sequence of moves will be incorrect, so only use this for tinyMaze
  """
  from game import Directions
  s = Directions.SOUTH
  w = Directions.WEST
  return  [s,s,w,s,w,w,s,w]

def depthFirstSearch(problem):
  """
  Search the deepest nodes in the search tree first
  [2nd Edition: p 75, 3rd Edition: p 87]
  
  Your search algorithm needs to return a list of actions that reaches
  the goal.  Make sure to implement a graph search algorithm 
  [2nd Edition: Fig. 3.18, 3rd Edition: Fig 3.7].
  
  To get started, you might want to try some of these simple commands to
  understand the search problem that is being passed in:
  
  print "Start:", problem.getStartState()
  print "Is the start a goal?", problem.isGoalState(problem.getStartState())
  print "Start's successors:", problem.getSuccessors(problem.getStartState())
  """
  "*** YOUR CODE HERE ***"
  #util.raiseNotDefined()
  print
  "the problem is ", problem
  from game import Directions
  s = Directions.SOUTH
  w = Directions.WEST
  n = Directions.NORTH
  e = Directions.EAST
  start = problem.getStartState()

  if problem.isGoalState(start):
      return []
  from util import Stack
  statesStack = Stack()
  exploredSet = set([start])
  tup = (start, [])
  statesStack.push(tup)
  while not statesStack.isEmpty():
      tup1 = statesStack.pop()
      state = tup1[0]
      path = tup1[1]
      if problem.isGoalState(state):
          return path
      successors = problem.getSuccessors(state)
      for succ in successors:
          coor = succ[0]
          move = succ[1]
          # cost = succ[2]
          tempPath = list(path)
          if not coor in exploredSet:
              exploredSet.add(coor)
              if move == 'North':
                  tempPath.append(n)
              elif move == 'East':
                  tempPath.append(e)
              elif move == 'South':
                  tempPath.append(s)
              elif move == 'West':
                  tempPath.append(w)
              statesStack.push((coor, tempPath))
              #print tempPath
              #print coor

  return []

def breadthFirstSearch(problem):
  """
  Search the shallowest nodes in the search tree first.
  [2nd Edition: p 73, 3rd Edition: p 82]
  """
  "*** YOUR CODE HERE ***"
  #util.raiseNotDefined()
  from game import Directions
  s = Directions.SOUTH
  w = Directions.WEST
  n = Directions.NORTH
  e = Directions.EAST
  start = problem.getStartState()
  print
  "the start state is ", start
  if problem.isGoalState(start):
      return []
  from util import Queue
  statesQueue = Queue()
  statesQueue.push((start, []))
  print
  "start is ", start
  exploredSet = set([start])
  while not statesQueue.isEmpty():
      tup1 = statesQueue.pop()
      state = tup1[0]
      path = tup1[1]
      if problem.isGoalState(state):
          return path
      successors = problem.getSuccessors(state)
      for succ in successors:
          succState = succ[0]
          move = succ[1]
          # cost = succ[2]
          tempPath = list(path)
          if not succState in exploredSet:
              exploredSet.add(succState)
              if move == 'North':
                  tempPath.append(n)
              elif move == 'East':
                  tempPath.append(e)
              elif move == 'South':
                  tempPath.append(s)
              elif move == 'West':
                  tempPath.append(w)
              statesQueue.push((succState, tempPath))
  return []

def uniformCostSearch(problem):
  "Search the node of least total cost first. "
  "*** YOUR CODE HERE ***"
  print
  "using my uniform cost!!"
  from game import Directions
  s = Directions.SOUTH
  w = Directions.WEST
  n = Directions.NORTH
  e = Directions.EAST
  start = problem.getStartState()
  if problem.isGoalState(start):
      return []
  from util import PriorityQueue
  statesQueue = PriorityQueue()
  statesQueue.push((start, [], 0), 0)
  exploredSet = set([start])
  while not statesQueue.isEmpty():
      tup1 = statesQueue.pop()
      # print "tup1 is ", tup1
      state = tup1[0]
      path = tup1[1]
      cost = tup1[2]
      if problem.isGoalState(state):
          return path
      successors = problem.getSuccessors(state)
      for succ in successors:
          coor = succ[0]
          move = succ[1]
          stepCost = succ[2]
          totalCost = cost + stepCost
          tempPath = list(path)
          if not coor in exploredSet:
              exploredSet.add(coor)
              if move == 'North':
                  tempPath.append(n)
              elif move == 'East':
                  tempPath.append(e)
              elif move == 'South':
                  tempPath.append(s)
              elif move == 'West':
                  tempPath.append(w)
              statesQueue.push((coor, tempPath, totalCost), totalCost)
  return []

def nullHeuristic(state, problem=None):
  """
  A heuristic function estimates the cost from the current state to the nearest
  goal in the provided SearchProblem.  This heuristic is trivial.
  """
  return 0

def aStarSearch(problem, heuristic=nullHeuristic):
  "Search the node that has the lowest combined cost and heuristic first."
  "*** YOUR CODE HERE ***"
  from game import Directions
  s = Directions.SOUTH
  w = Directions.WEST
  n = Directions.NORTH
  e = Directions.EAST
  start = problem.getStartState()
  if problem.isGoalState(start):
      return []
  from util import PriorityQueue
  statesQueue = PriorityQueue()
  statesQueue.push((start, []), 0)
  exploredSet = set([start])
  while not statesQueue.isEmpty():
      tup1 = statesQueue.pop()
      # print "tup1 is ", tup1
      state = tup1[0]
      path = tup1[1]
      if problem.isGoalState(state):
          return path
      successors = problem.getSuccessors(state)
      for succ in successors:
          coor = succ[0]
          move = succ[1]
          heuristicCost = heuristic(coor, problem)
          tempPath = list(path)
          if not coor in exploredSet:
              exploredSet.add(coor)
              if move == 'North':
                  tempPath.append(n)
              elif move == 'East':
                  tempPath.append(e)
              elif move == 'South':
                  tempPath.append(s)
              elif move == 'West':
                  tempPath.append(w)
              totalCost = problem.getCostOfActions(tempPath) + heuristicCost
              statesQueue.push((coor, tempPath), totalCost)
  return []
    
  
# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
