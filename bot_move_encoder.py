import json

from bot_move import BotMove

class BotMoveEncoder:

    @staticmethod
    def encode(botMove):
        data = {
            'Direction': botMove.moveDirection, 
            'Action': botMove.action, 
            'FireDirection': botMove.fireDirection
        }
        return json.dumps(data)
