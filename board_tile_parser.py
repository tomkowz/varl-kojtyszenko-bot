import json

from board_tile import BoardTile
from location import Location

class BoardTileParser:

    @staticmethod
    def get_tiles(data):
        tiles = []
        for tileData in data['Board']:
            location = Location(tileData[0], tileData[1])
            tileType = tileData[2]

            tile = BoardTile(location, tileType)
            tile.print_debug()
            tiles.append(tile)

        return tiles
