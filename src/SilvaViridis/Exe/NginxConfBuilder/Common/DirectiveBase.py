from abc import ABC
from typing import Self, Sequence

from .DirectiveDict import DirectiveDict

class DirectiveBase(ABC):
    def __init__(
        self,
        name : str,
        args : Sequence[str] = [],
        block : Sequence[Self | None] = [],
    ):
        self._name : str
        self.change_name(name)
        self._args : list[str] = list(args)
        self._block : list[Self | None] = list(block)

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
    ) -> Sequence[Self | None]:
        return self._block

    def change_name(
        self,
        value : str,
    ) -> None:
        self._name = value

    def add_arg(
        self,
        arg : str,
    ) -> None:
        # TODO: should we check that the items are repeated or not?
        self._args.append(arg)

    def add_directive(
        self,
        directive : Self,
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
