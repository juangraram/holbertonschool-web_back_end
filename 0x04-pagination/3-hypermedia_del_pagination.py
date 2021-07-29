#!/usr/bin/env python3
'''Deletion-resilient hypermedia pagination'''
from typing import List, Dict, Tuple
import csv
import math


class Server:
    '''Server class to paginate a database of popular baby names'''
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        '''Cached dataset'''
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        '''Sorting Index Dataset'''
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        '''Returns page info'''
        total_items = len(self.dataset())
        assert index < total_items
        data = []
        idx = index
        for _ in range(page_size):
            while not self.indexed_dataset().get(idx):
                idx += 1
            data.append([self.indexed_dataset().get(idx)])
            idx += 1

        return {
            "index": index,
            "next_index": idx,
            "page_size": page_size,
            "data": data
        }
