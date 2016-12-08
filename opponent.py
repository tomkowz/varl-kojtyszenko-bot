class Opponent:

    def __init__(self, location=None):
        self.location = location

    def print_debug(self):
        print "Opponent - pos: ({}, {})".format(int(self.location.x), int(self.location.y))