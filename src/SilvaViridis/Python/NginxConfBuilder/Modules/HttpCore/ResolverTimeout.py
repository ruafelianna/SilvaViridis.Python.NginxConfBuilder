from ...Common import DirectiveBase, TimeInterval, TimeIntervalGroup

DIR_RESOLVER_TIMEOUT = "resolver_timeout"

class ResolverTimeout(DirectiveBase):
    def __init__(
        self,
        order : int,
        time : TimeInterval | TimeIntervalGroup = TimeInterval(30),
    ):
        super().__init__(order, DIR_RESOLVER_TIMEOUT)
        self.add_arg(time)
