from ._DirectivesList import DIR_TCP_NOPUSH
from ...Common import DirectiveBase, OnOff

class TcpNopush(DirectiveBase):
    def __init__(
        self,
        state : OnOff = OnOff.off,
    ):
        super().__init__(DIR_TCP_NOPUSH)
        self.add_arg(state)
