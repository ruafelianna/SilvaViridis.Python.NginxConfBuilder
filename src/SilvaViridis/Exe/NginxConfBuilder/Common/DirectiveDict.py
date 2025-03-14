from typing import NotRequired, Self, Sequence, TypedDict

class DirectiveDict(TypedDict):
    directive : str
    args : Sequence[str]
    block : NotRequired[Sequence[Self]]
