from ...Common import DirectiveBase, PositiveSize, Size

DIR_POSTPONE_OUTPUT = "postpone_output"

class PostponeOutput(DirectiveBase):
    def __init__(
        self,
        order : int,
        size: PositiveSize | None = Size(value = 1460),
    ):
        super().__init__(order, DIR_POSTPONE_OUTPUT)
        self.add_arg(0 if size is None else size)
