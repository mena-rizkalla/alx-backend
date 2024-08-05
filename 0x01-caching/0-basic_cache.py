#!/usr/bin/python3
"""
   BasicCache module
"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ BasicCache class inherits from BaseCaching class
    """

    def __init__(self):
        """ Initialize BasicCache
        """
        super().__init__()

    def put(self, key, item):
        """ Assign data to cache_data dictionary
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """ implement get function
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
