from SilvaViridis.Python.Common.Types import PositiveInt

from ...Common import DirectiveBase, Variable

DIR_LIMIT_RATE = "limit_rate"

class LimitRate(DirectiveBase):
    def __init__(
        self,
        order : int,
        bps : PositiveInt | Variable | None = None,
    ):
        super().__init__(order, DIR_LIMIT_RATE)
        self.add_arg(0 if bps is None else bps)
