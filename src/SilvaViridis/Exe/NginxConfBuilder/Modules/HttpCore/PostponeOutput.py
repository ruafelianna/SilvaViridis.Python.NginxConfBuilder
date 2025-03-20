from ._DirectivesList import DIR_POSTPONE_OUTPUT
from ...Common import DirectiveBase, PositiveSize, Size

class PostponeOutput(DirectiveBase):
    def __init__(
        self,
        size: PositiveSize | None = Size(1460),
    ):
        super().__init__(DIR_POSTPONE_OUTPUT)
        self.add_arg(0 if size is None else size)
