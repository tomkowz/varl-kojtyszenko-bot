class GameConfig:

    def __init__(self, mapWidth=None, mapHeight=None, bombBlastRadius=None, 
        missileBlastRadius=None, roundsBetweenMissiles=None, 
        roundsBeforeIncreasingBlastRadius=None, isFastMissileModeEnabled=None):
        self.mapWidth = mapWidth
        self.mapHeight = mapHeight
        self.bombBlastRadius = bombBlastRadius
        self.missileBlastRadius = missileBlastRadius
        self.roundsBetweenMissiles = roundsBetweenMissiles
        self.roundsBeforeIncreasingBlastRadius = roundsBeforeIncreasingBlastRadius
        self.isFastMissileModeEnabled = isFastMissileModeEnabled

    def print_debug(self):
        print 'Config - map: ({}, {}), bomb radius: {}, missile radius: {}, rounds between missiles: {}'.format(
            int(self.mapWidth), int(self.mapHeight), int(self.bombBlastRadius), int(self.missileBlastRadius), int(self.roundsBetweenMissiles))
