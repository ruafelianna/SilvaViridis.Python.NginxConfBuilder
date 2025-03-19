from ._DirectivesList import (
    DIR_IF_MODIFIED_SINCE,
    T_IF_MODIFIED_SINCE__STATE,
    IF_MODIFIED_SINCE__STATE__EXACT,
)

from ...Common import DirectiveBase, OnOff

class IfModifiedSince(DirectiveBase):
    def __init__(
        self,
        state : T_IF_MODIFIED_SINCE__STATE = IF_MODIFIED_SINCE__STATE__EXACT,
    ):
        super().__init__(DIR_IF_MODIFIED_SINCE)

        if isinstance(state, OnOff):
            self.add_enum_arg(state)
        else:
            self.add_arg(state)

    @property
    def min_version(
        self,
    ) -> tuple[int, int, int]:
        return (0, 7, 24)
