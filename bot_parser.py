import json

from bot import Bot
from location import Location
from location_parser import get_location_from_string

class BotParser:
    
    @staticmethod
    def get_bot(data):
        pos = get_location_from_string(data['BotLocation'])
        location = Location(pos[0], pos[1])
        isMissileAvailable = bool(data['IsMissileAvailable'])
        bot = Bot(location, isMissileAvailable)
        bot.print_debug()
        return bot
