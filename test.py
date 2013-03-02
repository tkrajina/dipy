# -*- coding: utf-8 -*-

import di as mod_di

# ----------------------------------------------------------------------------------------------------
# DI objects:
# ----------------------------------------------------------------------------------------------------

class DBHandler:
    """ Object that will be "injected" in other objects """

    def handle_db(self):
        print 'I\'m handling some db stuff'

class ORMHandler:

    db_handler = mod_di.Dependency('dbhandler')

    def handle_orm(self):
        print 'I\'m handling some ORM stuff with my ', self.db_handler

# ----------------------------------------------------------------------------------------------------
# DI configuration:
# ----------------------------------------------------------------------------------------------------

class AppConfig:
    """
    Dependency injection configuration. Every DI object has a name 
    (representedt with a method name here).
    """

    def dbhandler(self):
        return DBHandler()

    def ormhandler(self):
        return ORMHandler()

mod_di.init(AppConfig)

# ----------------------------------------------------------------------------------------------------
# Usage:
# ----------------------------------------------------------------------------------------------------

class Test(object):
    """ Random object that need a DI handled object """

    orm_handler = mod_di.Dependency('ormhandler')

    def __init__(self):
        pass

test = Test()
test.orm_handler.handle_orm()

# Get a DI handled object directly:

orm_handler = mod_di.get('ormhandler')
orm_handler.handle_orm()
