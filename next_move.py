import random

from astar import AStar
from battlefield_info import BattlefieldInfo
from board_tile import BoardTile
from bomb import Bomb
from bot import Bot
from bot_action import BotAction
from bot_move import BotMove
from game_config import GameConfig
from location import Location
from missile import Missile
from move_direction import MoveDirection
from opponent import Opponent

class NextMove:

    def __init__(self, gameInfo=None, battlefieldInfo=None):
        self.gameInfo = gameInfo
        self.battlefieldInfo = battlefieldInfo

    def calculate(self):
        # Find path to opponent
        endLocation = self.battlefieldInfo.opponents[0].location
        astar = AStar(self.battlefieldInfo, endLocation)
        pathToOpponent = astar.get_path()

        moveDirection = MoveDirection.NoMove
        action = BotAction.NoAction

        # Calculate move direction based on first step of a shortest path to opponent
        if pathToOpponent is not None:
            moveDirection = self._calculate_move_direction(self.battlefieldInfo.bot.location, pathToOpponent[0])

            # Plant a bomb if bot is close to Opponent
            # Close mean in range of a bomb that bot can plant
            if len(pathToOpponent) <= self.battlefieldInfo.config.bombBlastRadius:
                action = BotAction.DropBomb

        fireDirection = self._calculate_fire_direction()

        botMove = BotMove(moveDirection, action, fireDirection)
        
        botMove.print_debug()
        return botMove

    def _calculate_move_direction(self, botLocation, nextLocation):
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

    def _calculate_fire_direction(self):
        return random.choice([
            MoveDirection.NoMove, 
            MoveDirection.Up, 
            MoveDirection.Down, 
            MoveDirection.Right, 
            MoveDirection.Left
            ])
    