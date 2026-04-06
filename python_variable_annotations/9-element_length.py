#!/usr/bin/env python3
"""Module for getting element lengths."""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Returns a list of tuples with elements and their lengths."""
    return [(i, len(i)) for i in lst]
