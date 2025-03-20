from __future__ import annotations

from typing import NotRequired, Sequence, TypedDict

class DirectiveDict(TypedDict):
    directive : str
    args : Sequence[str]
    block : NotRequired[Sequence[DirectiveDict]]
