from ...Common import DirectiveBase, OnOff

DIR_RESET_TIMEDOUT_CONNECTION = "reset_timedout_connection"

class ResetTimedoutConnection(DirectiveBase):
    def __init__(
        self,
        order : int,
        state : OnOff = OnOff.off,
    ):
        super().__init__(order, DIR_RESET_TIMEDOUT_CONNECTION)
        self.add_arg(state)
