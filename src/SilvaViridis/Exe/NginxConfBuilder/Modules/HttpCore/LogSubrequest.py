from ...Common import DirectiveBase, OnOff

DIR_LOG_SUBREQUEST = "log_subrequest"

class LogSubrequest(DirectiveBase):
    def __init__(
        self,
        state : OnOff = OnOff.off,
    ):
        super().__init__(DIR_LOG_SUBREQUEST)
        self.add_arg(state)
