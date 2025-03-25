from ...Common import DirectiveBase, PositiveSize, Size

DIR_POSTPONE_OUTPUT = "postpone_output"

class PostponeOutput(DirectiveBase):
    def __init__(
        self,
        size: PositiveSize | None = Size(1460),
    ):
        super().__init__(DIR_POSTPONE_OUTPUT)
        self.add_arg(0 if size is None else size)
