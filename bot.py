class Bot:

    def __init__(self, location=None, isMissileAvailable=None):
        self.location = location
        self.isMissileAvailable = isMissileAvailable

    def print_debug(self):
        print 'Bot - pos: ({}, {})'.format(int(self.location.x), int(self.location.y))