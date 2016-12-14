import random

from astar import Node, NodeMetadata
from location import Location

class EscapeLocation:

    def __init__(self, battlefieldInfo, botLocation, opponentLocation, nodes):
        self.battlefieldInfo = battlefieldInfo
        self.botLocation = botLocation
        self.opponentLocation = opponentLocation
        self.nodes = nodes

    def calculateEscapeLocation(self):
        mapWidth = self.battlefieldInfo.config.mapWidth - 1
        mapHeight = self.battlefieldInfo.config.mapHeight - 1
        corner = random.randint(0, 3)

        corner0 = Location(0, 0)
        corner1 = Location(mapWidth - 1, 0)
        corner2 = Location(mapWidth - 1, mapHeight - 1)
        corner3 = Location(0, mapHeight - 1)

        iterations = min(mapWidth, mapHeight) / 2

        found = False
        for k in range(iterations):
            for i in range(4):
                corner = None
                if i == 0:
                    corner = corner0
                elif i == 1:
                    corner = corner1
                elif i == 2:
                    corner = corner2
                elif i == 3:
                    corner = corner3

                if self.nodes[corner.x][corner.y].metadata.isAvailable == True:
                    # Return location if found good one to escape
                    return corner
                else:
                    if i == 0:
                        x = min(max(0, corner.x + 1), mapWidth)
                        y = min(max(0, corner.y + 1), mapHeight)
                        corner0 = Location(x, y)
                    if i == 1:
                        x = min(max(0, corner.x - 1), mapWidth)
                        y = min(max(0, corner.y + 1), mapHeight)
                        corner1 = Location(x, y)
                    if i == 2:
                        x = min(max(0, corner.x - 1), mapWidth)
                        y = min(max(0, corner.y - 1), mapHeight)
                        corner2 = Location(x, y)
                    if i == 3:
                        x = min(max(0, corner.x + 1), mapWidth)
                        y = min(max(0, corner.y - 1), mapHeight)
                        corner3 = Location(x, y)   

        return None
