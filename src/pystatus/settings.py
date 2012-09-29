# -*- coding: utf-8 -*-
class Configuration(object):
    DATABASE = {
        'name': 'systemstatus.db',
        'engine': 'peewee.SqliteDatabase',
        'check_same_thread': False,
    }
    DEBUG = True,
    SECRET_KEY = '12345678'
