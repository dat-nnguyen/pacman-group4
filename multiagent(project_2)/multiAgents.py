# multiAgents.py
# --------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


from util import manhattanDistance
from game import Directions
import random, util

from game import Agent
from pacman import GameState

class ReflexAgent(Agent):
    """
    A reflex agent chooses an action at each choice point by examining
    its alternatives via a state evaluation function.

    The code below is provided as a guide.  You are welcome to change
    it in any way you see fit, so long as you don't touch our method
    headers.
    """


    def getAction(self, gameState: GameState):
        """
        You do not need to change this method, but you're welcome to.

        getAction chooses among the best options according to the evaluation function.

        Just like in the previous project, getAction takes a GameState and returns
        some Directions.X for some X in the set {NORTH, SOUTH, WEST, EAST, STOP}
        """
        # Collect legal moves and successor states
        legalMoves = gameState.getLegalActions()

        # Choose one of the best actions
        scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
        bestScore = max(scores)
        bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
        chosenIndex = random.choice(bestIndices) # Pick randomly among the best

        "Add more of your code here if you want to"

        return legalMoves[chosenIndex]

    def evaluationFunction(self, currentGameState: GameState, action):
        """
        Design a better evaluation function here.

        The evaluation function takes in the current and proposed successor
        GameStates (pacman.py) and returns a number, where higher numbers are better.

        The code below extracts some useful information from the state, like the
        remaining food (newFood) and Pacman position after moving (newPos).
        newScaredTimes holds the number of moves that each ghost will remain
        scared because of Pacman having eaten a power pellet.

        Print out these variables to see what you're getting, then combine them
        to create a masterful evaluation function.
        """
        # Useful information you can extract from a GameState (pacman.py)
        successorGameState = currentGameState.generatePacmanSuccessor(action)
        newPos = successorGameState.getPacmanPosition()
        newFood = successorGameState.getFood()
        newGhostStates = successorGameState.getGhostStates()
        newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]

        # "*** YOUR CODE HERE ***"
        # return successorGameState.getScore()
        
        # Lay danh sach thuc an va vien nang con lai
        foodList = newFood.asList()
        capsules = successorGameState.getCapsules()

        # Bat dau bang diem cua trang thai tiep theo
        score = successorGameState.getScore()

        # Uu tien di den thuc an gan nhat
        if foodList:
            minFoodDistance = min(
                manhattanDistance(newPos, food)
                for food in foodList
            )
            score += 10.0 / (minFoodDistance + 1)

        # Danh gia khoang cach den cac con ma
        for ghostState in newGhostStates:
            ghostPos = ghostState.getPosition()
            ghostDistance = manhattanDistance(newPos, ghostPos)

            if ghostState.scaredTimer > 0:
                # Chi khuyen khich duoi ma neu con du thoi gian
                if ghostState.scaredTimer > ghostDistance:
                    score += 10.0 / (ghostDistance + 1)
            else:
                # Tranh ma dang nguy hiem
                if ghostDistance <= 1:
                    score -= 200
                elif ghostDistance == 2:
                    score -= 20

        # Uu tien vien nang khi can thiet
        if capsules:
            minCapsuleDistance = min(
                manhattanDistance(newPos, capsule)
                for capsule in capsules
            )
            score += 3.0 / (minCapsuleDistance + 1)

        # Han che dung yen
        if action == Directions.STOP:
            score -= 10

        return score


def scoreEvaluationFunction(currentGameState: GameState):
    """
    This default evaluation function just returns the score of the state.
    The score is the same one displayed in the Pacman GUI.

    This evaluation function is meant for use with adversarial search agents
    (not reflex agents).
    """
    return currentGameState.getScore()

class MultiAgentSearchAgent(Agent):
    """
    This class provides some common elements to all of your
    multi-agent searchers.  Any methods defined here will be available
    to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

    You *do not* need to make any changes here, but you can if you want to
    add functionality to all your adversarial search agents.  Please do not
    remove anything, however.

    Note: this is an abstract class: one that should not be instantiated.  It's
    only partially specified, and designed to be extended.  Agent (game.py)
    is another abstract class.
    """

    def __init__(self, evalFn = 'scoreEvaluationFunction', depth = '2'):
        self.index = 0 # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)

class MinimaxAgent(MultiAgentSearchAgent):
    """
    Your minimax agent (question 2)
    """

    def getAction(self, gameState: GameState):
        """
        Returns the minimax action from the current gameState using self.depth
        and self.evaluationFunction.

        Here are some method calls that might be useful when implementing minimax.

        gameState.getLegalActions(agentIndex):
        Returns a list of legal actions for an agent
        agentIndex=0 means Pacman, ghosts are >= 1

        gameState.generateSuccessor(agentIndex, action):
        Returns the successor game state after an agent takes an action

        gameState.getNumAgents():
        Returns the total number of agents in the game

        gameState.isWin():
        Returns whether or not the game state is a winning state

        gameState.isLose():
        Returns whether or not the game state is a losing state
        """
        "*** YOUR CODE HERE ***"
        util.raiseNotDefined()

class AlphaBetaAgent(MultiAgentSearchAgent):
    """
    Your minimax agent with alpha-beta pruning (question 3)
    """

    def getAction(self, gameState: GameState):
        """
        Returns the minimax action using self.depth and self.evaluationFunction
        """
        "*** YOUR CODE HERE ***"
        util.raiseNotDefined()


class ExpectimaxAgent(MultiAgentSearchAgent):
    """
      Your expectimax agent (question 4)
    """

    def getAction(self, gameState: GameState):
        """
        Returns the expectimax action using self.depth and self.evaluationFunction.
        Ghosts are modeled as choosing uniformly at random from legal actions.
        """
        numAgents = gameState.getNumAgents()

        def expectimax(state, agentIndex, depth):
            if state.isWin() or state.isLose() or depth == self.depth:
                return self.evaluationFunction(state)

            actions = state.getLegalActions(agentIndex)
            if not actions:
                return self.evaluationFunction(state)

            nextAgent = agentIndex + 1
            nextDepth = depth
            if nextAgent == numAgents:
                nextAgent = 0
                nextDepth += 1

            values = [
                expectimax(state.generateSuccessor(agentIndex, action), nextAgent, nextDepth)
                for action in actions
            ]

            if agentIndex == 0:
                return max(values)
            return sum(values) / len(values)

        legalActions = gameState.getLegalActions(0)
        if not legalActions:
            return Directions.STOP

        return max(
            legalActions,
            key=lambda action: expectimax(
                gameState.generateSuccessor(0, action),
                1 if numAgents > 1 else 0,
                0
            )
        )



def betterEvaluationFunction(currentGameState: GameState):
    """
    Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
    evaluation function (question 5).

    DESCRIPTION: <write something here so we know what you did>
    """
    if currentGameState.isWin():
        return float("inf")
    if currentGameState.isLose():
        return float("-inf")

    pacmanPos = currentGameState.getPacmanPosition()
    food = currentGameState.getFood().asList()
    capsules = currentGameState.getCapsules()
    ghostStates = currentGameState.getGhostStates()
    score = currentGameState.getScore()

    # Encourage Pacman to approach the nearest remaining food.
    if food:
        nearestFoodDist = min(manhattanDistance(pacmanPos, foodPos) for foodPos in food)
        score += 20.0 / (nearestFoodDist + 1)
        score -= 3.0 * len(food)

    # Capsules are useful, especially when active ghosts are nearby.
    if capsules:
        nearestCapsuleDist = min(manhattanDistance(pacmanPos, pos) for pos in capsules)
        activeGhostNearby = any(
            ghost.scaredTimer == 0 and
            manhattanDistance(pacmanPos, ghost.getPosition()) <= 5
            for ghost in ghostStates
        )
        score += (8.0 if activeGhostNearby else 2.0) / (nearestCapsuleDist + 1)
        score -= 5.0 * len(capsules)

    # Avoid active ghosts; approach scared ghosts only while time permits.
    for ghost in ghostStates:
        ghostPos = ghost.getPosition()
        if ghostPos is None:
            continue
        ghostDist = manhattanDistance(pacmanPos, ghostPos)
        if ghost.scaredTimer > 0:
            if ghost.scaredTimer > ghostDist:
                score += 8.0 / (ghostDist + 1)
        elif ghostDist == 0:
            score -= 500.0
        elif ghostDist == 1:
            score -= 300.0
        elif ghostDist == 2:
            score -= 100.0
        elif ghostDist ==3:
            score -= 50.0

    return score

# Abbreviation
better = betterEvaluationFunction
