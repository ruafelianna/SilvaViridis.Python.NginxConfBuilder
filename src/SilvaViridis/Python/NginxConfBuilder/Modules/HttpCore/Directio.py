from typing import Literal

from ...Common import DirectiveBase, OnOff, Size

DIR_DIRECTIO = "directio"

class Directio(DirectiveBase):
    def __init__(
        self,
        order : int,
        state : Size | Literal[OnOff.off] = OnOff.off,
    ):
        super().__init__(order, DIR_DIRECTIO)
        self.add_arg(state)

    @property
    def min_version(
        self,
    ) -> tuple[int, int, int]:
        return (0, 7, 7)
