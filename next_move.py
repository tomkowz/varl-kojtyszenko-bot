import random

from astar import AStar
from battlefield_info import BattlefieldInfo
from board_tile import BoardTile
from bomb import Bomb
from bot import Bot
from bot_action import BotAction
from bot_move import BotMove
from escape_location import EscapeLocation
from game_config import GameConfig
from location import Location
from missile import Missile
from move_direction import MoveDirection
from opponent import Opponent

escapeLocation = None

class NextMoveInfo:
    
    def __init__(self, botMove, nextLocation):
        self.botMove = botMove
        self.nextLocation = nextLocation

class NextMove:

    def __init__(self, gameInfo=None, battlefieldInfo=None):
        self.gameInfo = gameInfo
        self.battlefieldInfo = battlefieldInfo

    def calculate(self):
        global escapeLocation
        opponentLocation = self.battlefieldInfo.opponents[0].location
        # Find path to desired position
        # If escape location is specified then bot is running away
        # otherwise it tries to go to the opponent.
        endLocation = None
        if escapeLocation is None:
            endLocation = opponentLocation
        else:
            endLocation = escapeLocation
        
        # Find a path
        astar = AStar(self.battlefieldInfo, endLocation)
        (pathToFollow, nodes) = astar.get_path()

        moveDirection = MoveDirection.NoMove
        action = BotAction.NoAction
        fireDirection = MoveDirection.Up

        nextMoveLocation = None
        # Calculate move direction based on first step of a shortest path to opponent
        if pathToFollow is not None and len(pathToFollow) > 0:
            nextMoveLocation = pathToFollow[0]
            moveDirection = self._get_move_direction(self.battlefieldInfo.bot.location, nextMoveLocation)

            if escapeLocation is not None:
                # If you hit escape location in next move you have to go to the opponent next round
                if nextMoveLocation.x == escapeLocation.x and nextMoveLocation.y == escapeLocation.y:
                    escapeLocation = None
            else:
                # If you're following opponent then you need to calculate some action, probably...                    
                didAction = False
                # Check whether way to opponent is a straight line (for new step) without any obstacles.
                # If that's true then make fire a missile.
                if self._is_straight_line(pathToFollow):
                    action = BotAction.FireMissile
                    fireDirection = self._get_fire_direction(pathToFollow)
                    didAction = True

                # Plant a bomb if bot is close to Opponent
                # Close mean in range of a bomb that bot can plant
                if len(pathToFollow) <= self.battlefieldInfo.config.bombBlastRadius:
                    action = BotAction.DropBomb
                    didAction = True

                # If action is performed, then bot want to escape to a safe area next time
                if didAction is True:
                    # Find an escape position
                    escapeLocationFinder = EscapeLocation(self.battlefieldInfo, nextMoveLocation, opponentLocation, nodes)
                    escapeLocation = escapeLocationFinder.calculateEscapeLocation()
                    if escapeLocation is not None:
                        print 'Escaping to: ({}, {})'.format(escapeLocation.x, escapeLocation.y)
                    else:
                        print 'Cannot find escape location'

        botMove = BotMove(moveDirection, action, fireDirection)
        botMove.print_debug()

        # Return structure that contains info to be returned by the server and info
        # what is the next location of the bot, so it can decide what next.
        nextMoveInfo = NextMoveInfo(botMove, nextMoveLocation)
        return nextMoveInfo

    def _get_move_direction(self, botLocation, nextLocation):
        if botLocation.x + 1 == nextLocation.x:
            return MoveDirection.Right
        elif botLocation.x - 1 == nextLocation.x:
            return MoveDirection.Left
        elif botLocation.y - 1 == nextLocation.y:
            return MoveDirection.Up
        elif botLocation.y + 1 == nextLocation.y:
            return MoveDirection.Down
        else:
            return MoveDirection.NoMove

    def _get_fire_direction(self, path):
        start = path[0]
        end = path[-1]

        if start.x < end.x:
            return MoveDirection.Right
        elif start.x > end.x:
            return MoveDirection.Left
        elif start.y < end.y:
            return MoveDirection.Down
        else:
            return MoveDirection.Up

    def _is_straight_line(self, path):
        start = path[0]
        end = path[-1]

        isStraight = True
        current = path[0]
        for element in path:
            if current.x == element.x:
                current = element
            else:
                isStraight = False
                break

        if isStraight == True:
            return True

        current = path[0]
        for element in path:
            if current.y == element.y:
                current = element
            else:
                isStraight = False
                break

        if isStraight == True:
            return True
        else:
            return False
