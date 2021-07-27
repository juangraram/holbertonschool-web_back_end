#!/usr/bin/env python3
"""Class BasicCache"""

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """Class BasicCache is a caching system"""

    def put(self, key, item):
        """Method put"""
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """Method get"""
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        else:
            return None
