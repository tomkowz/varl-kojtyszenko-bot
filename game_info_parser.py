import json

from game_info import GameInfo

class GameInfoParser:

    @staticmethod
    def get_info(data):
        roundNumber = int(data['RoundNumber'])
        info = GameInfo(roundNumber)
        info.print_debug()
        return info