from ...Common import DirectiveBase, Size, Variable

DIR_LIMIT_RATE_AFTER = "limit_rate_after"

class LimitRateAfter(DirectiveBase):
    def __init__(
        self,
        order : int,
        size : Size | Variable = Size(value = 0),
    ):
        super().__init__(order, DIR_LIMIT_RATE_AFTER)
        self.add_arg(size)

    @property
    def min_version(
        self,
    ) -> tuple[int, int, int]:
        return (0, 8, 0)
