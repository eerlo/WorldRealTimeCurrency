#-*- coding: utf-8 -*-
from .backends import BCBBackend
class WorldCurrency(object):
    def __init__(self):
        self.backend = BCBBackend()
        self._currencies = {}
        self.update_values()
    def update_values(self):
        self._currencies = self.backend.get_currencies()

    def get_currency(self, code):
        return self._currencies.get(code, None)

    def get_backend(self):
        return self.backend

    def set_backend(self, backend):
        self.backend = backend