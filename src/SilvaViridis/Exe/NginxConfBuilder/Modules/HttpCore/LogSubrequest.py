from ._DirectivesList import DIR_LOG_SUBREQUEST
from ...Common import DirectiveBase, OnOff

class LogSubrequest(DirectiveBase):
    def __init__(
        self,
        state : OnOff = OnOff.off,
    ):
        super().__init__(DIR_LOG_SUBREQUEST)
        self.add_arg(state)
