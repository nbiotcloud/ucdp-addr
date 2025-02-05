"""Access Type Description."""

from enum import Enum


class TransType(Enum):
    """Trans Type."""

    SINGLE = 0
    BURST = 1
    SCAT = 2

    def __repr__(self):
        return self.name


def get_transtype(data, noscat=False):
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
    if isinstance(data, (tuple, list)):
        if isinstance(data[0], (tuple, list)):
            if noscat:
                raise TypeError("Scattered Data is not supported")
            return TransType.SCAT
        return TransType.BURST
    return TransType.SINGLE
