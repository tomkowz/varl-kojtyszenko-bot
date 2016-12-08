class GameInfo:

    def __init__(self, roundNumber=None):
        self.roundNumber = roundNumber

    def print_debug(self):
        print 'Info - round: {}'.format(int(self.roundNumber))
