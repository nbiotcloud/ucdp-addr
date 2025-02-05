"""Access Type Description."""

from enum import Enum
from typing import TypeAlias


class TransType(Enum):
    """Trans Type."""

    SINGLE = 0
    BURST = 1
    SCAT = 2

    def __repr__(self):
        return self.name


Data: TypeAlias = int | tuple[int, ...] | list[int] | tuple[tuple[int, int], ...] | list[tuple[int, int]]


def get_transtype(data: Data, noscat: bool = False):
    """
    Determine :any:`Access` of `data`.

    >>> get_transtype(1)
    SINGLE
    >>> get_transtype((1, 2, 3))
    BURST
    >>> get_transtype([1, 2, 3])
    BURST
    >>> get_transtype([(1, 8), (2, 9), (3, 10)])
    SCAT
    >>> get_transtype([(1, 8), (2, 9), (3, 10)], noscat=True)
    Traceback (most recent call last):
      ...
    TypeError: Scattered Data is not supported
    """
    if isinstance(data, int):
        return TransType.SINGLE
    if isinstance(data, (tuple, list)):
        if all(isinstance(item, int) for item in data):
            return TransType.BURST
        if all(isinstance(item, tuple) and len(item) == 2 for item in data):  # noqa: PLR2004
            if noscat:
                raise TypeError("Scattered Data is not supported")
            return TransType.SCAT
    raise TypeError(data)
