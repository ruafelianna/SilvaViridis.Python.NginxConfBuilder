from ...Common import DirectiveBase, Size

DIR_READ_AHEAD = "read_ahead"

class ReadAhead(DirectiveBase):
    def __init__(
        self,
        size: Size = Size(0),
    ):
        super().__init__(DIR_READ_AHEAD)
        self.add_arg(size)
