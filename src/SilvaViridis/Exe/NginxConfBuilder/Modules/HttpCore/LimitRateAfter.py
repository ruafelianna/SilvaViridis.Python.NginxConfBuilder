from ._DirectivesList import DIR_LIMIT_RATE_AFTER
from ...Common import DirectiveBase, Size, Variable

class LimitRateAfter(DirectiveBase):
    def __init__(
        self,
        size : Size | Variable = Size(0),
    ):
        super().__init__(DIR_LIMIT_RATE_AFTER)
        self.add_arg(size)

    @property
    def min_version(
        self,
    ) -> tuple[int, int, int]:
        return (0, 8, 0)
