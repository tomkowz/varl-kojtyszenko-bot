#!/usr/bin/env python
# -*- coding: utf-8 -*-

from board_tile_type import BoardTileType

class BattlefieldInfo:

    def __init__(self, bot=None, tiles=None, opponents=None, bombs=None, missiles=None, config=None):
        self.bot = bot
        self.tiles = tiles
        self.opponents = opponents
        self.bombs = bombs
        self.missiles = missiles
        self.config = config

    def print_board(self):
        items = [['·' for col in range(0, self.config.mapWidth)] for row in range(0, self.config.mapHeight)]
       
        # Collect tiles
        for tile in self.tiles:
            if tile.tileType != BoardTileType.Empty:
                items[tile.location.x][tile.location.y] = tile.tileType

        # Collect bot
        items[self.bot.location.x][self.bot.location.y] = '×'

        # Collect opponents
        for opponent in self.opponents:
            items[opponent.location.x][opponent.location.y] = '■'

        # Collect bombs
        for bomb in self.bombs:
            items[bomb.location.x][bomb.location.y] = 'b'

        # Collect missiles
        for missile in self.missiles:
            items[missile.location.x][missile.location.y] = 'm'

        # Draw board
        for col in range(0, self.config.mapWidth):
            for row in range(0, self.config.mapHeight):
                print items[row][col],
            print ''
        