#!/usr/bin/env python
# -*- coding: utf-8 -*-

validator = None

class NinValidator(object):
    def __init__(self, arg):
        super(NinValidator, self).__init__()
        self.arg = arg
        self._nin = None

    def set_country(self, country):
        try:
            validator = importlib.import_module('nin.validators.%s' % (country))
        except:
            raise Exception('Unable to load validator for specified country: %s' % (country))

    @property
    def nin(self):
        return self._nin

    @nin.setter
    def nin(self, value):
        self._nin = value
