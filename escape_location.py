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

        corners = [
            Location(0, 0),
            Location(mapWidth - 1, 0),
            Location(mapWidth - 1, mapHeight - 1),
            Location(0, mapHeight - 1)
        ]

        iterations = min(mapWidth, mapHeight)

        found = False
        for k in range(iterations):
            for i in range(4):
                location = corners[i]
                if self.nodes[location.x][location.y].metadata.isAvailable == True:
                    # Return location if found good one to escape
                    return location
                else:
                    if i == 0:
                        corners[0] = Location(min(max(0, location.x + 1), mapWidth), min(max(0, location.y + 1), mapHeight))
                    if i == 1:
                        corners[1] = Location(min(max(0, location.x - 1), mapWidth), min(max(0, location.y + 1, mapHeight)))
                    if i == 2:
                        corners[2] = Location(min(max(0, location.x - 1), mapWidth), min(max(0, location.y - 1, mapHeight)))
                    if i == 3:
                        corners[3] = Location(min(max(0, location.x + 1), mapWidth), min(max(0, location.y - 1, mapHeight)))   

        return None
