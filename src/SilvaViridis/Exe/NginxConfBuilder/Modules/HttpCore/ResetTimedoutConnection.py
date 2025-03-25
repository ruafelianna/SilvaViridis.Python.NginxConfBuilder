from ...Common import DirectiveBase, OnOff

DIR_RESET_TIMEDOUT_CONNECTION = "reset_timedout_connection"

class ResetTimedoutConnection(DirectiveBase):
    def __init__(
        self,
        state : OnOff = OnOff.off,
    ):
        super().__init__(DIR_RESET_TIMEDOUT_CONNECTION)
        self.add_arg(state)
