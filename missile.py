class Missile:

    def __init__(self, moveDirection=None, location=None, explosionRadius=None):
        self.moveDirection = moveDirection
        self.location = location
        self.explosionRadius = explosionRadius

    def print_debug(self):
        print 'Missile - direction: {}, pos: ({}, {}), radius: {}'.format(int(self.moveDirection), 
            int(self.location.x), int(self.location.y), int(self.explosionRadius))
