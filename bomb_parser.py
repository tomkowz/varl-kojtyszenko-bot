import json

from bomb import Bomb
from location import Location
from location_parser import get_location_from_string

class BombParser:

    @staticmethod
    def get_bombs(data):
        bombs = []
        for bombData in data['Bombs']:
            roundsUntilExplodes = int(bombData['RoundsUntilExplodes'])
            parsedLocation = get_location_from_string(bombData['Location'])
            location = Location(parsedLocation[0], parsedLocation[1])
            explosionRadius = int(bombData['ExplosionRadius'])

            bomb = Bomb(roundsUntilExplodes, location, explosionRadius)
            bomb.print_debug()
            bombs.append(bomb)

        return bombs