#!/usr/bin/env python
# -*- coding: utf-8 -*-

from board_tile import BoardTile
from board_tile_type import BoardTileType
from bomb import Bomb
from bot import Bot
from game_config import GameConfig
from location import Location
from missile import Missile
from move_direction import MoveDirection
from opponent import Opponent

class Node:
    
    def __init__(self, location=None):
        self.location = location
        self.metadata = NodeMetadata()
        self.parent = None
        self.g = 10
        self.h = None

    @property
    def f(self):
        return self.g + self.h

class NodeMetadata:
    
    def __init__(self):
        self.isAvailable = True
        self.isBomb = False
        self.isMissile = False
        self.isShortestPath = False

    def markBomb(self, isAvailable):
        self.isBomb = True
        self.isMissile = False
        self.isShortestPath = False
        self.isAvailable = isAvailable

    def markMissile(self, isAvailable):
        self.isMissile = True
        self.isBomb = False
        self.isShortestPath = False
        self.isAvailable = isAvailable

    def markShortestPath(self):
        self.isShortestPath = True
        self.isBomb = False
        self.isMissile = False
        self.isAvailable = True

    def markUnavailable(self):
        self.isAvailable = False
        self.isBomb = False
        self.isMissile = False
        self.isShortestPath = False

class AStar:
    
    def __init__(self, battlefieldInfo, endLocation):
        self.battlefieldInfo = battlefieldInfo
        self.startLocation = battlefieldInfo.bot.location
        self.endLocation = endLocation
        self.mapWidth = battlefieldInfo.config.mapWidth
        self.mapHeight = battlefieldInfo.config.mapHeight
        self.nodes = []

    def get_path(self):
        # Create nodes that represent every field on the board
        self.nodes = []
        
        for col in range(0, self.mapWidth):
            nodesInRow = []
            for row in range(0, self.mapHeight):
                location = Location(col, row);
                node = Node(location)
                nodesInRow.append(node)
            self.nodes.append(nodesInRow)
            
        self._add_tiles()
        self._add_bombs()
        self._add_missiles()

        shortestPath = self._calculate_shortest_path()
        self._add_shortest_path(shortestPath)

        self._print_debug()

        return (shortestPath, self.nodes)

    def _calculate_shortest_path(self):
        # Create first node and mark it as unvisited
        startNode = self.nodes[self.startLocation.x][self.startLocation.y]
        unvisited = [startNode]
        visited = []

        # Iterate through unvisited nodes until all are checked
        currentNode = None
        while len(unvisited) != 0:
            # This is first iteration and we just want to take the only
            # one element in unvisited array
            if currentNode is None:
                currentNode = unvisited[0]
            else:
                # find node with minimum f value
                currentNode = unvisited[0]
                for candidate in unvisited:
                    if candidate.f < currentNode.f:
                        currentNode = candidate
            
            # Get adjacents of the current node
            adjacents = [
                self._get_adjacent_node_if_exist(currentNode.location, 0, -1),
                self._get_adjacent_node_if_exist(currentNode.location, 1, 0),
                self._get_adjacent_node_if_exist(currentNode.location, 0, 1),
                self._get_adjacent_node_if_exist(currentNode.location, -1, 0)
            ]
            
            # Remove None nodes, not available and visited ones
            adjacents = filter(lambda x: x is not None, adjacents)

            # print 'Found adjacents:',
            # for adjacent in adjacents:
            #     print '({}, {}, {})'.format(adjacent.location.x, adjacent.location.y, adjacent.metadata.isAvailable),

            #     if adjacent.metadata.isAvailable == False:
            #         print 'b: {}, m: {}'.format(adjacent.metadata.isBomb, adjacent.metadata.isMissile)
            # print ''

            adjacents = filter(lambda x: x.metadata.isAvailable == True, adjacents)
            adjacents = filter(lambda x: x not in visited, adjacents)
            
            for adjacent in adjacents:
                # Add adjacent to unvisited if not in there yet
                if adjacent not in unvisited:
                    unvisited.append(adjacent)
                
                # Calculate Manhattan distance and if this is a first calculation for an adjacent
                # just store the value and set parrent, otherwise do check whether
                # the adjacent can be accessed with lower cost.
                distance = self._calculate_manhattan_distance(adjacent.location, self.endLocation) * 10
                if adjacent.h is None:
                    adjacent.h = distance
                    adjacent.parent = currentNode

                else:
                    if distance < adjacent.h:
                        adjacent.h = distance    
                        adjacent.parent = currentNode

                # print 'cn: ({}, {}), adj: ({}, {})'.format(currentNode.location.x, currentNode.location.y,
                    # adjacent.location.x, adjacent.location.y)

            # Remove selected node from unvisited
            unvisited.remove(currentNode)

            # Add the current node to list of visited
            visited.append(currentNode)
            
            # Check whether current node is the destination Node
            if (currentNode.location.x == self.endLocation.x and currentNode.location.y == self.endLocation.y):
                path = []
                while currentNode.parent is not None:
                    path.insert(0, currentNode.location)
                    currentNode = currentNode.parent
                return path

        # If path not found then return empty array
        return []

    def _get_adjacent_node_if_exist(self, location, dX, dY):
        x = max(0, min(location.x + dX, self.mapWidth - 1))
        y = max(0, min(location.y + dY, self.mapHeight - 1))
        if location.x == x and location.y == y:
            return None
        return self.nodes[x][y]

    def _calculate_manhattan_distance(self, locationA, locationB):
        distance = 0
        if locationA.x > locationB.x:
            distance += abs(locationA.x - locationB.x)
        else:
            distance += abs(locationB.x - locationA.x)

        if locationA.y > locationB.y:
            distance += abs(locationA.y - locationB.y)
        else:
            distance += abs(locationB.y - locationA.y)    

        return distance

    def _add_tiles(self):
        for tile in self.battlefieldInfo.tiles:
            node = self.nodes[tile.location.x][tile.location.y]
            node.metadata.isAvailable = tile.tileType == BoardTileType.Empty

    def _add_bombs(self):
        for bomb in self.battlefieldInfo.bombs:
            radius = bomb.explosionRadius

            node = self.nodes[bomb.location.x][bomb.location.y]
            node.metadata.markBomb(isAvailable=False)

            # Mark unavailable fields based on radius and number of rounds until it explodes.
            # Bot can go through the range of the bomb if it has a time to run away before it explodes.
            # Every round the range will increase so bot has less chance to be in a bomb range.
            offsetMax = max(0, (radius - (bomb.roundsUntilExplodes - 2)) + 1)

            for offset in range(0, offsetMax):
                explodingNodes = [
                    self.nodes[max(0, bomb.location.x - offset)][bomb.location.y],
                    self.nodes[min(bomb.location.x + offset, self.mapWidth - 1)][bomb.location.y],
                    self.nodes[bomb.location.x][max(0, bomb.location.y - offset)],
                    self.nodes[bomb.location.x][min(bomb.location.y + offset, self.mapHeight - 1)]
                ]
                
                for explodingNode in explodingNodes:
                    explodingNode.metadata.markBomb(isAvailable=False)

    def _add_missiles(self):
        for missile in self.battlefieldInfo.missiles:
            radius = missile.explosionRadius

            node = self.nodes[missile.location.x][missile.location.y]

            if missile.moveDirection == MoveDirection.Up:
                vector = (0, -1)

            elif missile.moveDirection == MoveDirection.Right:
                vector = (1, 0)

            elif missile.moveDirection == MoveDirection.Down:
                vector = (0, 1)

            elif missile.moveDirection == MoveDirection.Left:
                vector = (-1, 0)

            # Go through nodes untill inavailable node is found so it means
            # that's the target of a missile
            location = node.location

            while self.nodes[location.x][location.y].metadata.isAvailable == True:
                # The trajectory of missile is available to go through
                self.nodes[location.x][location.y].metadata.markMissile(isAvailable=False)

                col = max(0, min(location.x + vector[0], self.mapWidth - 1))
                row = max(0, min(location.y + vector[1], self.mapHeight - 1))

                if ((row == 0 and vector[1] == -1) or 
                    (row == self.mapHeight - 1 and vector[1] == 1) or 
                    (col == 0 and vector[0] == -1) or 
                    (col == self.mapWidth - 1 and vector[0] == 1)):
                        self.nodes[location.x][location.y].metadata.markMissile(isAvailable=False)

                location = Location(col, row)

            # mark missile position as unavailable
            self.nodes[missile.location.x][missile.location.y].metadata.markMissile(isAvailable=False)

            # Mark missile explosion
            for offset in range(0, radius + 1):
                explodingNodes = [
                    self.nodes[max(0, location.x - offset)][location.y],
                    self.nodes[min(location.x + offset, self.mapWidth - 1)][location.y],
                    self.nodes[location.x][max(0, location.y - offset)],
                    self.nodes[location.x][min(location.y + offset, self.mapHeight - 1)]
                ]

                for explodingNode in explodingNodes:
                    explodingNode.metadata.markMissile(isAvailable=False)

    def _add_shortest_path(self, path):
        for location in path:
            print '({}, {})'.format(location.x, location.y),
            self.nodes[location.x][location.y].metadata.markShortestPath()

    def _print_debug(self):
        print 'Get Path >>>>>>'
        for row in range(0, self.mapHeight):
            for col in range(0, self.mapWidth):
                node = self.nodes[col][row]
                if node.metadata.isAvailable == True:
                    if self.startLocation.x == col and self.startLocation.y == row:
                        print '×',
                    elif self.endLocation.x == col and self.endLocation.y == row:
                        print '■',
                    elif node.metadata.isShortestPath == True:
                        print '♦',
                    else:
                        print '·',
                        
                else:
                    if node.metadata.isBomb == True:
                        print 'b',
                    elif node.metadata.isMissile == True:
                        print 'm',
                    else:
                        print 'W',
                # print '({}, {}) -> ({}, {})'.format(col, row, node.location.x, node.location.y)
            print ''
    
        print 'Get Path <<<<<<'
