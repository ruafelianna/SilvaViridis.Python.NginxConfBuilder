from typing import Literal

from ._DirectivesList import DIR_IF_MODIFIED_SINCE
from ...Common import DirectiveBase, OnOff

class IfModifiedSince(DirectiveBase):
    def __init__(
        self,
        state : Literal[OnOff.off, "exact", "before"] = "exact",
    ):
        super().__init__(DIR_IF_MODIFIED_SINCE)
        self.add_arg(state)

    @property
    def min_version(
        self,
    ) -> tuple[int, int, int]:
        return (0, 7, 24)
