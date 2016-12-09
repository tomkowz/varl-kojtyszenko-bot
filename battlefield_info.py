#!/usr/bin/env python
# -*- coding: utf-8 -*-

class BattlefieldInfo:

    def __init__(self, bot=None, tiles=None, opponents=None, bombs=None, missiles=None, config=None):
        self.bot = bot
        self.tiles = tiles
        self.opponents = opponents
        self.bombs = bombs
        self.missiles = missiles
        self.config = config

    def print_board(self):
        items = [['·' for i in range(0, self.config.mapWidth)] for i in range(0, self.config.mapHeight)]
       
        # Collect tiles
        for tile in self.tiles:
            items[tile.location.x][tile.location.y] = '{}'.format(tile.tileType)

        # Collect bot
        items[self.bot.location.x][self.bot.location.y] = 'b'

        # Collect opponents
        for opponent in self.opponents:
            items[opponent.location.x][opponent.location.y] = 'o'

        # Collect bombs
        for bomb in self.bombs:
            items[bomb.location.x][bomb.location.y] = '⨂'

        # Collect missiles
        for missile in self.missiles:
            items[missile.location.x][missile.location.y] = '⨀'

        # Draw board
        for i in range(0, self.config.mapWidth):
            for j in range(0, self.config.mapHeight):
                print items[i][j],
            print ''
        