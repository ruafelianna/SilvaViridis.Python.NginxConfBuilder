from typing import Literal

from ...Common import DirectiveBase, OnOff

DIR_IF_MODIFIED_SINCE = "if_modified_since"

class IfModifiedSince(DirectiveBase):
    def __init__(
        self,
        order : int,
        state : Literal[OnOff.off, "exact", "before"] = "exact",
    ):
        super().__init__(order, DIR_IF_MODIFIED_SINCE)
        self.add_arg(state)

    @property
    def min_version(
        self,
    ) -> tuple[int, int, int]:
        return (0, 7, 24)
