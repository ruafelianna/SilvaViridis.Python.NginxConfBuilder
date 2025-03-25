from ...Common import DirectiveBase, OnOff

DIR_TCP_NOPUSH = "tcp_nopush"

class TcpNopush(DirectiveBase):
    def __init__(
        self,
        state : OnOff = OnOff.off,
    ):
        super().__init__(DIR_TCP_NOPUSH)
        self.add_arg(state)
