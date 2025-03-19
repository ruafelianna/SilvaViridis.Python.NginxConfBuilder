from ._DirectivesList import DIR_LOG_NOT_FOUND
from ...Common import DirectiveBase, OnOff

class LogNotFound(DirectiveBase):
    def __init__(
        self,
        state : OnOff = OnOff.on,
    ):
        super().__init__(DIR_LOG_NOT_FOUND)
        self.add_arg(state)
