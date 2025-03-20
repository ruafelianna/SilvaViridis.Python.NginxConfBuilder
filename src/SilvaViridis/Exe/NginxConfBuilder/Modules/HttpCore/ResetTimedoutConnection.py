from ._DirectivesList import DIR_RESET_TIMEDOUT_CONNECTION
from ...Common import DirectiveBase, OnOff

class ResetTimedoutConnection(DirectiveBase):
    def __init__(
        self,
        state : OnOff = OnOff.off,
    ):
        super().__init__(DIR_RESET_TIMEDOUT_CONNECTION)
        self.add_arg(state)
