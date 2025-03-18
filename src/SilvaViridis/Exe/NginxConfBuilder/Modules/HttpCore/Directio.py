from typing import Literal

from .DirectivesList import DIR_DIRECTIO
from ...Common import DirectiveBase, OnOff, Size

class Directio(DirectiveBase):
    def __init__(
        self,
        state : Size | Literal[OnOff.off] = OnOff.off,
    ):
        super().__init__(DIR_DIRECTIO)

        if isinstance(state, Size):
            self.add_arg(state)
        else:
            self.add_enum_arg(state)

    @property
    def min_version(
        self,
    ) -> tuple[int, int, int]:
        return (0, 7, 7)
