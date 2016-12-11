import json

from board_tile import BoardTile
from location import Location

class BoardTileParser:

    @staticmethod
    def get_tiles(data, mapWidth, mapHeight):
        tiles = []

        for col in range(0, mapWidth):
            for row in range(0, mapHeight):
                location = Location(col, row)
                tileType = data['Board'][row][col]
                tile = BoardTile(location, tileType)
                # tile.print_debug()
                tiles.append(tile)
        return tiles 
