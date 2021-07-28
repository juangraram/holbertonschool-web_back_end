#!/usr/bin/env python3
"""Simple helper function pagination"""
import csv
import math
from typing import Tuple, List, Dict


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Method return a tuple of size two containing a
        start index and an end index"""
    start = ((page - 1) * page_size)
    end = page * page_size
    return start, end


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """method named get_page"""
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page > 0
        rang = index_range(page, page_size)
        server = Server()
        start = rang[0]
        end = rang[1]
        if end > len(server.dataset()):
            return []
        return server.dataset()[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """returns data set pagination info"""
        dataset_items = len(self.dataset())
        data = self.get_page(page, page_size)
        total_pages = math.ceil(dataset_items / page_size)

        ret = {
            "page": page,
            "page_size": page_size if page < total_pages else 0,
            "data": data,
            "next_page": page + 1 if page + 1 < total_pages else None,
            "prev_page": page - 1 if page - 1 > 0 else None,
            "total_pages": total_pages
        }
        return ret
