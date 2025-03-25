from SilvaViridis.Python.Common.Types import PositiveInt

from ...Common import DirectiveBase

DIR_MAX_RANGES = "max_ranges"

class MaxRanges(DirectiveBase):
    def __init__(
        self,
        quantity : PositiveInt | None = None,
    ):
        super().__init__(DIR_MAX_RANGES)
        self.add_arg(0 if quantity is None else quantity)

    @property
    def min_version(
        self,
    ) -> tuple[int, int, int]:
        return (1, 1, 2)
