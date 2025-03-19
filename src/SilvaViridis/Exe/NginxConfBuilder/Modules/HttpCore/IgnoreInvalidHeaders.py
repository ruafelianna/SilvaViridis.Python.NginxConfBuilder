from ._DirectivesList import DIR_IGNORE_INVALID_HEADERS
from ...Common import DirectiveBase, OnOff

class IgnoreInvalidHeaders(DirectiveBase):
    def __init__(
        self,
        state : OnOff = OnOff.on,
    ):
        super().__init__(DIR_IGNORE_INVALID_HEADERS)
        self.add_arg(state)
