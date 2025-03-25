from typing import Literal

from ...Common import DirectiveBase, OnOff

DIR_LINGERING_CLOSE = "lingering_close"

class LingeringClose(DirectiveBase):
    def __init__(
        self,
        order : int,
        state : OnOff | Literal["always"] = OnOff.on,
    ):
        super().__init__(order, DIR_LINGERING_CLOSE)
        self.add_arg(state)

    @property
    def min_version(
        self,
    ) -> tuple[int, int, int]:
        return (1, 0, 6)
