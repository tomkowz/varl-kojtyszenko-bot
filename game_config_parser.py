import json

from game_config import GameConfig

class GameConfigParser:

    @staticmethod
    def get_config(data):
        configData = data['GameConfig']
        mapWidth = int(configData['MapWidth'])
        mapHeight = int(configData['MapHeight'])
        bombBlastRadius = int(configData['BombBlastRadius'])
        missileBlastRadius = int(configData['MissileBlastRadius'])
        roundsBetweenMissiles = int(configData['RoundsBetweenMissiles'])
        roundsBeforeIncreasingBlastRadius = int(configData['RoundsBeforeIncreasingBlastRadius'])
        isFastMissileModeEnabled = bool(configData['IsFastMissileModeEnabled'])

        config = GameConfig(mapWidth, mapHeight, bombBlastRadius, missileBlastRadius, roundsBetweenMissiles,
            roundsBeforeIncreasingBlastRadius, isFastMissileModeEnabled)
        config.print_debug()
        
        return config