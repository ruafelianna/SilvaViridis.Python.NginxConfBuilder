from ._DirectivesList import DIR_LIMIT_RATE
from ...Common import DirectiveBase, PositiveInt, Variable

class LimitRate(DirectiveBase):
    def __init__(
        self,
        bps : PositiveInt | Variable | None = None,
    ):
        super().__init__(DIR_LIMIT_RATE)
        self.add_arg(0 if bps is None else bps)
