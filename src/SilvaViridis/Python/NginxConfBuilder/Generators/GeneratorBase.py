from abc import ABC
from collections.abc import Callable, Sequence

from ..Common import (
    DirectiveBase,
    DirectiveDict,
)

from ..Modules import MainContext

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
        result = directive.build()
        if isinstance(directive, MainContext):
            if "block" in result:
                return self._to_str(result["block"])
            else:
                raise ValueError("Main context is empty!")
        else:
            return self._to_str((result,))
