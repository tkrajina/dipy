# -*- coding: utf-8 -*-

import pdb

DI_OBJECTS = {}

class Dependency(object):
    """
    Property descriptor for dependency injection.
    """

    def __init__(self, di_object_name):
        self.di_object_name = di_object_name

    def __get__(self, obj, objtype):
        if not DI_OBJECTS.has_key(self.di_object_name):
            raise AttributeError, 'Unknown dependency object name %s' % self.di_object_name

        return DI_OBJECTS[self.di_object_name]

    def __set__(self, obj, value):
        raise AttributeError, "can't set attribute"

    def __delete__(self, obj):
        raise AttributeError, "can't delete attribute"

def init(dependency_conf):
    dependency_descriptor = dependency_conf()
    for di_object_name in dir(dependency_descriptor):
        if not di_object_name.startswith('_'):
            attr = getattr(dependency_descriptor, di_object_name)
            if callable(attr):
                di_object = attr()
                DI_OBJECTS[di_object_name] = di_object
    # TODO: Check for cyclical dependencies!

def get(di_object_name):
    if not DI_OBJECTS.has_key(di_object_name):
        raise Exception, 'Unknown dependency object name %s' % di_object_name
    return DI_OBJECTS[di_object_name]
