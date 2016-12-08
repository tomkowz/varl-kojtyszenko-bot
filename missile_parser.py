import json

from location import Location
from location_parser import get_location_from_string
from missile import Missile

class MissileParser:

    @staticmethod
    def get_missiles(data):
        missiles = []

        for missileData in data['Missiles']:
            moveDirection = int(missileData['MoveDirection'])
            parsedLocation = get_location_from_string(missileData['Location'])
            location = Location(parsedLocation[0], parsedLocation[1])
            explosionRadius = int(missileData['ExplosionRadius'])

            missile = Missile(moveDirection, location, explosionRadius)
            missile.print_debug()
            missiles.append(missile)

        return missiles
