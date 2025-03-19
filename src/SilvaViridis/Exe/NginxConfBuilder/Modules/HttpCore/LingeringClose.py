from typing import Literal

from ._DirectivesList import DIR_LINGERING_CLOSE
from ...Common import DirectiveBase, OnOff

class LingeringClose(DirectiveBase):
    def __init__(
        self,
        state : OnOff | Literal["always"] = OnOff.on,
    ):
        super().__init__(DIR_LINGERING_CLOSE)
        self.add_arg(state)

    @property
    def min_version(
        self,
    ) -> tuple[int, int, int]:
        return (1, 0, 6)
