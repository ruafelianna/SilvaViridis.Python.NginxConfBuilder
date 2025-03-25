from ...Common import DirectiveBase, OnOff

DIR_TCP_NODELAY = "tcp_nodelay"

class TcpNodelay(DirectiveBase):
    def __init__(
        self,
        order : int,
        state : OnOff = OnOff.on,
    ):
        super().__init__(order, DIR_TCP_NODELAY)
        self.add_arg(state)
