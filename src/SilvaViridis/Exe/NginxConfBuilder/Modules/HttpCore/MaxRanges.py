from annotated_types import Gt
from typing import Annotated

from ._DirectivesList import DIR_MAX_RANGES
from ...Common import DirectiveBase

class MaxRanges(DirectiveBase):
    def __init__(
        self,
        quantity : Annotated[int, Gt(0)] | None = None,
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
