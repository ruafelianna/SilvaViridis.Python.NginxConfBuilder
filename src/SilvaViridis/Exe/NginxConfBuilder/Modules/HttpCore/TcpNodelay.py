from ...Common import DirectiveBase, OnOff

DIR_TCP_NODELAY = "tcp_nodelay"

class TcpNodelay(DirectiveBase):
    def __init__(
        self,
        state : OnOff = OnOff.on,
    ):
        super().__init__(DIR_TCP_NODELAY)
        self.add_arg(state)
