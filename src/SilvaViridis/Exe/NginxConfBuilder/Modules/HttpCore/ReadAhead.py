from ._DirectivesList import DIR_READ_AHEAD
from ...Common import DirectiveBase, Size

class ReadAhead(DirectiveBase):
    def __init__(
        self,
        size: Size = Size(0),
    ):
        super().__init__(DIR_READ_AHEAD)
        self.add_arg(size)
