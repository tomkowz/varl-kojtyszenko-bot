import json

from location import Location
from location_parser import get_location_from_string
from opponent import Opponent

class OpponentParser:

    @staticmethod
    def get_opponents(data):
        opponents = []
        opponentLocations = data['OpponentLocations']
        for locationString in opponentLocations:
            parsedLocation = get_location_from_string(locationString)
            location = Location(parsedLocation[0], parsedLocation[1])
            opponent = Opponent(location)
            opponent.print_debug()
            opponents.append(opponent)

        return opponents
