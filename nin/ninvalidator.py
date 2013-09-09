#!/usr/bin/env python
# -*- coding: utf-8 -*-

import importlib

class NinValidator(object):
    _validator = None

    def __init__(self, country=None, nin=None):
        self._nin = None
        self._validator = None
        if country:
            self.set_country(country)
        if nin:
            self.nin = nin

    def set_country(self, country):
        self._validator = importlib.import_module('nin.validators.%s' % (country))
        try:
            pass
        except:
            raise Exception('Unable to load validator for specified country: %s' % (country))

    @property
    def nin(self):
        return self._nin

    @nin.setter
    def nin(self, value):
        self._nin = value

    @property
    def age(self):
        if not self._validator:
            return None
        return self._validator.get_age(self._nin)

    @property
    def valid(self):
        if not self._validator:
            return False
        return self._validator.is_valid(self._nin)

    @property
    def sanitize(self):
        if not self._validator:
            return None
        return self._validator.sanitize(self._nin)
