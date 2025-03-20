from ._DirectivesList import DIR_LIMIT_RATE
from ...Common import DirectiveBase, PositiveInt, Variable

class LimitRate(DirectiveBase):
    def __init__(
        self,
        bps : PositiveInt | Variable | None = None,
    ):
        super().__init__(DIR_LIMIT_RATE)

        if bps is None:
            self.add_arg(0)
        else:
            self.add_arg(bps)
