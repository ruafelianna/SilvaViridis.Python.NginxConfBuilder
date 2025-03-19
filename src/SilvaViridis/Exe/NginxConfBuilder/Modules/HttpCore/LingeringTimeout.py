from ._DirectivesList import DIR_LINGERING_TIMEOUT
from ...Common import DirectiveBase, TimeInterval, TimeIntervalGroup

class LingeringTimeout(DirectiveBase):
    def __init__(
        self,
        time : TimeInterval | TimeIntervalGroup = TimeInterval(5),
    ):
        super().__init__(DIR_LINGERING_TIMEOUT)
        self.add_arg(time)
