class BotMove:

    def __init__(self, moveDirection=None, action=None, fireDirection=None):
        self.moveDirection = moveDirection
        self.action = action
        self.fireDirection = fireDirection

    def print_debug(self):
        print 'BotMove - move direction: {}, action: {}, fire direction: {}'.format(self.moveDirection, self.action, 
            self.fireDirection)
