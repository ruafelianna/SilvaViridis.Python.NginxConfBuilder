from ._DirectivesList import DIR_TCP_NODELAY
from ...Common import DirectiveBase, OnOff

class TcpNodelay(DirectiveBase):
    def __init__(
        self,
        state : OnOff = OnOff.on,
    ):
        super().__init__(DIR_TCP_NODELAY)
        self.add_arg(state)
