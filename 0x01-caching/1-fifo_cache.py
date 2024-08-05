#!/usr/bin/python3
""" implement FIFOCache """
from base_caching import (BaseCaching)


class FIFOCache(BaseCaching):
    """ Implement FIFOCache """

    def __init__(self):
        """ Initialize the FIFOCache"""
        super().__init__()
        self.order = []

    def put(self, key, item):
        """ Add an item to the cache """
        if key is None or item is None:
            return

        if key not in self.cache_data:
            self.order.append(key)
        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            # remove first item from cache_data
            oldest_key = self.order.pop(0)
            del self.cache_data[oldest_key]
            print(f"DISCARD: {oldest_key}")

        def get(self, key):
            """ get an item from the cache """
            if key is None or key not in self.cache_data:
                return
            return self.cache_data[key]
