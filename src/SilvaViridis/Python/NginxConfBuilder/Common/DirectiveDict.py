from __future__ import annotations

from collections.abc import Sequence
from typing import NotRequired, TypedDict

class DirectiveDict(TypedDict):
    directive : str
    args : Sequence[str]
    block : NotRequired[Sequence[DirectiveDict]]
