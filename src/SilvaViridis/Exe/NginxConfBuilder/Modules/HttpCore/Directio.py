from typing import Literal

from ._DirectivesList import DIR_DIRECTIO
from ...Common import DirectiveBase, OnOff, Size

class Directio(DirectiveBase):
    def __init__(
        self,
        state : Size | Literal[OnOff.off] = OnOff.off,
    ):
        super().__init__(DIR_DIRECTIO)
        self.add_arg(state)

    @property
    def min_version(
        self,
    ) -> tuple[int, int, int]:
        return (0, 7, 7)
