#!/usr/bin/env python3
"""Module for creating a key-value tuple with squared value."""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Returns a tuple with the string and the square of the number."""
    return (k, float(v ** 2))
