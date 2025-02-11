#
# MIT License
#
# Copyright (c) 2024 nbiotcloud
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#
"""Unified Chip Design Platform - Address Map."""

from .access import (
    ACCESSES,
    Access,
    ReadOp,
    ToAccess,
    WriteOp,
    cast_access,
    get_counteraccess,
)
from .addrdecoder import AddrDecoder
from .addrinfo import AddrInfo
from .addrmap import AddrMap, create_fill_addrspace
from .addrmapfinder import Defines, GetAttrspacesFunc, get_addrmap, get_addrspaces
from .addrmaster import AddrMaster
from .addrmatrix import AddrMatrix
from .addrrange import AddrRange
from .addrref import AddrRef
from .addrslave import AddrSlave
from .addrspace import (
    Addrspace,
    DefaultAddrspace,
    Field,
    ReservedAddrspace,
    Word,
    Words,
    create_fill_field,
    create_fill_word,
)
from .addrspacealias import AddrspaceAlias
from .addrspaces import Addrspaces, join_addrspaces, zip_addrspaces
from .const import NOREF
from .data import DataType
from .datainfo import DataInfo
from .resolver import resolve
from .util import calc_depth_size
from .wordinfo import WordInfo

__all__ = [
    "ACCESSES",
    "NOREF",
    "Access",
    "AddrDecoder",
    "AddrInfo",
    "AddrMap",
    "AddrMaster",
    "AddrMatrix",
    "AddrRange",
    "AddrRef",
    "AddrSlave",
    "Addrspace",
    "AddrspaceAlias",
    "Addrspaces",
    "DataInfo",
    "DataType",
    "DefaultAddrspace",
    "Defines",
    "Field",
    "GetAttrspacesFunc",
    "ReadOp",
    "ReservedAddrspace",
    "ToAccess",
    "Word",
    "WordInfo",
    "Words",
    "WriteOp",
    "calc_depth_size",
    "cast_access",
    "create_fill_addrspace",
    "create_fill_field",
    "create_fill_word",
    "get_addrmap",
    "get_addrspaces",
    "get_counteraccess",
    "join_addrspaces",
    "resolve",
    "zip_addrspaces",
]
