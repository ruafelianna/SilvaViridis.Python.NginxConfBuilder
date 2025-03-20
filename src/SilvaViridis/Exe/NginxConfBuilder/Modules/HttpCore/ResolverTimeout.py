from ._DirectivesList import DIR_RESOLVER_TIMEOUT
from ...Common import DirectiveBase, TimeInterval, TimeIntervalGroup

class ResolverTimeout(DirectiveBase):
    def __init__(
        self,
        time : TimeInterval | TimeIntervalGroup = TimeInterval(30),
    ):
        super().__init__(DIR_RESOLVER_TIMEOUT)
        self.add_arg(time)
