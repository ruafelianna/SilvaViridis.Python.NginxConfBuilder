from ._DirectivesList import DIR_MAX_RANGES
from ...Common import DirectiveBase, PositiveInt

class MaxRanges(DirectiveBase):
    def __init__(
        self,
        quantity : PositiveInt | None = None,
    ):
        super().__init__(DIR_MAX_RANGES)

        if quantity is None:
            self.add_arg(0)
        else:
            self.add_arg(quantity)

    @property
    def min_version(
        self,
    ) -> tuple[int, int, int]:
        return (1, 1, 2)
