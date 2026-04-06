#!/usr/bin/env python3
"""Module for creating a multiplier function."""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Returns a function that multiplies a float by multiplier."""

    def multiplier_func(x: float) -> float:
        """Multiplies x by the outer multiplier."""
        return x * multiplier

    return multiplier_func
