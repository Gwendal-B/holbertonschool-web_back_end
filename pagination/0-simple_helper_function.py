#!usr/bin/env python3
"""
Module providing a helper function for pagination.
"""

def index_range(page: int, page_size: int) -> tuple:
    """
    Returns a tuple of size two containing the start index
    and end index for a given pagination page and page size.

    Args:
        page (int): The current page number (1-indexed).
        page_size (int): The number of items per page.

    Returns:
        tuple: A tuple (start_index, end_index).
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size

    return (start_index, end_index)
