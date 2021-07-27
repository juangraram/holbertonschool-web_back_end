#!/usr/bin/env python3

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """BaseCaching (Parent class)"""
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """Put a item"""
        if key and item:
            self.cache_data.update({key: item})

    def get(self, key):
        """Return a value linked to a key"""
        if key in self.cache_data:
            return self.cache_data[key]
        return None
