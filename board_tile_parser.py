import json

from board_tile import BoardTile
from location import Location

class BoardTileParser:

    @staticmethod
    def get_tiles(data):
        tiles = []
        boardData = data['Board']
        rows = len(boardData)
        cols = len(boardData[0])

        for x in range(0, rows):
            for y in range(0, cols):
                location = Location(x, y)
                tileType = boardData[x][y];

                tile = BoardTile(location, tileType)
                tile.print_debug()
                tiles.append(tile)

        return tiles
