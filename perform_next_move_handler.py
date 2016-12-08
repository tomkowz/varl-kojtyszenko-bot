#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import tornado.web

from battlefield_info import BattlefieldInfo
from bomb import Bomb
from bomb_parser import BombParser
from bot import Bot
from bot_action import BotAction
from bot_move import BotMove
from bot_move_encoder import BotMoveEncoder
from bot_parser import BotParser
from board_tile import BoardTile
from board_tile_parser import BoardTileParser
from board_tile_type import BoardTileType
from game_config import GameConfig
from game_config_parser import GameConfigParser
from game_info import GameInfo
from game_info_parser import GameInfoParser
from missile import Missile
from missile_parser import MissileParser
from move_direction import MoveDirection
from next_move import NextMove
from opponent import Opponent
from opponent_parser import OpponentParser

class PerformNextMoveHandler(tornado.web.RequestHandler):

    def set_default_headers(self):
        self.set_header('Content-Type', 'application/json')

    def post(self):
        print '<<<<<<'
        data = json.loads(self.request.body)

        gameInfo = GameInfoParser.get_info(data)
        bot = BotParser.get_bot(data)
        tiles = BoardTileParser.get_tiles(data)
        opponents = OpponentParser.get_opponents(data)
        bombs = BombParser.get_bombs(data)
        missiles = MissileParser.get_missiles(data)
        config = GameConfigParser.get_config(data)

        battlefieldInfo = BattlefieldInfo(bot, tiles, opponents, bombs, missiles, config)
        nextMove = NextMove(gameInfo, battlefieldInfo)
        botMove = nextMove.calculate()
        print '>>>>>>'

        response = BotMoveEncoder.encode(botMove)
        self.write(response)

    def _calculate_next_move(self):
        return BotMove(None, BotAction.DropBomb, MoveDirection.Up)
