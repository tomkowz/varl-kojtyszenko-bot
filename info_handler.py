#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import tornado.web

class InfoHandler(tornado.web.RequestHandler):

    def set_default_headers(self):
        self.set_header('Content-Type', 'application/json')

    def get(self):
        response = {
            'Name': 'tomkowz',
            'AvatarUrl': 'http://szulctomasz.com/avatars/avatar-3-300-300.png',
            'Description': r'Ram pam pam, jeb jeb jeb, nie śpimy, lecimy!',
            'GameType': 'TankBlaster'
        }
        self.write(json.dumps(response))