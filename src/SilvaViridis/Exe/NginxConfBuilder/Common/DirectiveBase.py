from __future__ import annotations

from abc import ABC
from beartype import beartype
from enum import Enum
from typing import Callable, Sequence

from SilvaViridis.Python.Common.Enums import OrderedEnum
from SilvaViridis.Python.Common.Web import HttpStatus, MimeType

from ._ValidatorsList import NonEmptyString
from .DirectiveDict import DirectiveDict

@beartype
class DirectiveBase(ABC):
    def __init__(
        self,
        name : NonEmptyString,
        args : Sequence[NonEmptyString] = [],
        block : Sequence[DirectiveBase | None] = [],
    ):
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
                else:
                    result = str(value)
            else:
                result = to_str(value)

            self._args.append(f"{prefix}{result}")

    def add_directive(
        self,
        directive : DirectiveBase,
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

        if len(self.block) > 0:
            result["block"] = [b.build() for b in self.block if b]

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
