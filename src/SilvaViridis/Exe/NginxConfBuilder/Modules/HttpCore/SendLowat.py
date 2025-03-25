from ...Common import DirectiveBase, Size

DIR_SEND_LOWAT = "send_lowat"

class SendLowat(DirectiveBase):
    def __init__(
        self,
        size: Size = Size(0),
    ):
        super().__init__(DIR_SEND_LOWAT)
        self.add_arg(size)
