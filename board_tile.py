class BoardTile:

    def __init__(self, location=None, tileType=None):
        self.location = location
        self.tileType = tileType

    def print_debug(self):
        print 'Tile - pos: ({}, {}), type: {}'.format(int(self.location.x), int(self.location.y), int(self.tileType))
