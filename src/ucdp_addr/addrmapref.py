"""Module, Word and Field Reference."""

from functools import cached_property
from typing import TypeAlias

import ucdp as u

from .addrrange import AddrRange
from .addrspace import Addrspace, Field, Word


class AddrMapRef(u.Object):
    """Address Map Reference."""

    addrspace: Addrspace
    """Address Space."""

    word: Word | None = None
    """Word."""

    field: Field | None = None
    """Field."""

    def __str__(self) -> str:
        result = f"{self.addrspace.name}"
        if self.word:
            result = f"{result}.{self.word.name}"
            if self.field:
                result = f"{result}.{self.field.name}"
        return result

    @cached_property
    def addrrange(self) -> AddrRange:
        """Address Range."""
        addrspace = self.addrspace
        word = self.word
        if word:
            return AddrRange(
                baseaddr=addrspace.baseaddr + word.byteoffset,
                width=word.width,
                depth=word.depth or 1,
            )
        return AddrRange(baseaddr=addrspace.baseaddr, width=addrspace.width, depth=addrspace.depth)


RawAddrMapRef: TypeAlias = AddrMapRef | Addrspace | str
"""Unresolved Address Map Reference."""
