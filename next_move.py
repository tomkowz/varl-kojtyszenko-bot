import random

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
        moveDirection = self._calculate_move_direction()
        action = self._calculate_action()
        fireDirection = self._calculate_fire_direction()

        botMove = BotMove(moveDirection, action, fireDirection)
        
        botMove.print_debug()
        return botMove

    def _calculate_move_direction(self):
        return random.choice([
            MoveDirection.NoMove, 
            MoveDirection.Up, 
            MoveDirection.Down, 
            MoveDirection.Right, 
            MoveDirection.Left
            ])

    def _calculate_action(self):
        options = [BotAction.NoAction, BotAction.DropBomb]
        if self.battlefieldInfo.bot.isMissileAvailable is True:
            options.append(BotAction.FireMissile)

        return random.choice(options)

    def _calculate_fire_direction(self):
        return random.choice([
            MoveDirection.Up, 
            MoveDirection.Down, 
            MoveDirection.Right, 
            MoveDirection.Left
            ])
    