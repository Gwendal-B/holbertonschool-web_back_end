#!/usr/bin/env python3
"""
Module providing a helper function for pagination.
"""

import csv
from typing import List, Tuple


def index_range(page: int, page_size: int) -> tuple[int, int]:
    """
    Returns a tuple of size two containing the start index
    and end index for a given pagination page and page size.

    Args:
        page (int): The current page number (1-indexed).
        page_size (int): The number of items per page.

    Returns:
        tuple: A tuple (start_index, end_index).
    """
    start = (page - 1) * page_size
    end = page * page_size

    return (start, end)


class Server:
    """
    Server class to paginate a database of popular baby names.
    """

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self) -> None:
        """
        This method initializes the server instance.
        """
        self.__dataset = None

    def dataset(self) -> List[List[str]]:
        """
        This method loads and caches the dataset.
        """
        if self.__dataset is None:
            with open(self.DATA_FILE, encoding="utf-8") as file:
                reader = csv.reader(file)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]
        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List[str]]:
        """
        This method returns the appropriate page of the dataset.
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        start, end = index_range(page, page_size)
        dataset = self.dataset()

        if start >= len(dataset):
            return []

        return dataset[start:end]
