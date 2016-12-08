class Bomb:

    def __init__(self, roundsUntilExplodes=None, location=None, explosionRadius=None):
        self.roundsUntilExplodes = roundsUntilExplodes
        self.location = location
        self.explosionRadius = explosionRadius

    def print_debug(self):
        print 'Bomb - explodes in: {}, pos: ({}, {}), radius: {}'.format(int(self.roundsUntilExplodes), 
            int(self.location.x), int(self.location.y), int(self.explosionRadius))