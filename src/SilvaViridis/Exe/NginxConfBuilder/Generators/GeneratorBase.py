from abc import ABC
from typing import Callable, Sequence

from ..Common import (
    DirectiveBase,
    DirectiveDict,
)

class GeneratorBase(ABC):
    def __init__(
        self,
        to_str : Callable[[Sequence[DirectiveDict]], str],
    ):
        self._to_str = to_str

    def build(
        self,
        directive : DirectiveBase,
    ) -> str:
        return self._to_str((directive.build(),))

    def build_many(
        self,
        directives : Sequence[DirectiveBase],
    ) -> str:
        return self._to_str(tuple((d.build() for d in directives)))
