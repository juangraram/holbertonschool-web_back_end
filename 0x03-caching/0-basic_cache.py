#!/usr/bin/env python3

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):

    def put(self, key, item):
        """Put a item"""
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """Return a value linked to a key"""
        if key in self.cache_data:
            return self.cache_data[key]
        return None
