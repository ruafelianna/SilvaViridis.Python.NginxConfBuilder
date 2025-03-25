from __future__ import annotations

from abc import ABC
from beartype import beartype
from collections.abc import Callable, Sequence
from enum import Enum

from SilvaViridis.Python.Common.Enums import OrderedEnum
from SilvaViridis.Python.Common.Types import NonEmptyString
from SilvaViridis.Python.Common.Web import HttpStatus, MimeType

from .DirectiveDict import DirectiveDict

@beartype
class DirectiveBase(ABC):
    def __init__(
        self,
        order : int,
        name : NonEmptyString,
        args : Sequence[NonEmptyString] = [],
        block : Sequence[DirectiveBase | None] = [],
    ):
        self._order = order
        self._name : str
        self.change_name(name)
        self._args : list[str] = list(args)
        self._block : list[DirectiveBase | None] = list(block)

    @property
    def name(
        self,
    ) -> str:
        return self._name

    @property
    def args(
        self,
    ) -> Sequence[str]:
        return self._args

    @property
    def block(
        self,
    ) -> Sequence[DirectiveBase | None]:
        return self._block

    @property
    def min_version(
        self,
    ) -> tuple[int, int, int]:
        return (0, 0, 0)

    def change_name(
        self,
        value : NonEmptyString,
    ) -> None:
        self._name = value

    def add_arg[T](
        self,
        value : T | None,
        prefix : str = "",
        to_str : Callable[[T], str] | None = None,
    ) -> None:
        if value is not None:
            result : str

            if to_str is None:
                if isinstance(value, Enum):
                    result = DirectiveBase._to_str__enum(value)
                elif isinstance(value, bool):
                    if value:
                        result = ""
                    else:
                        return
                else:
                    result = str(value)
            else:
                result = to_str(value)

            self._args.append(f"{prefix}{result}")

    def add_directive(
        self,
        directive : DirectiveBase | None,
    ) -> None:
        if directive == self:
            raise ValueError("Cannot add itself to the list of directives to prevent cyclic references. Please, make a copy of an object.")
        self._block.append(directive)

    def build(
        self,
    ) -> DirectiveDict:
        result : DirectiveDict = {
            "directive": self.name,
            "args": self.args,
        }

        def sort_directives(directive : DirectiveBase) -> int:
            return directive._order

        directives = [b for b in self.block if b]
        directives = sorted(directives, key = sort_directives)

        if len(self.block) > 0:
            result["block"] = [d.build() for d in directives]

        return result

    @staticmethod
    def _to_str__enum(
        obj : Enum,
    ) -> str:
        if isinstance(obj, (
            OrderedEnum,
            HttpStatus,
            MimeType,
        )):
            return str(obj.value)
        return obj.name
