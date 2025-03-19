from ._DirectivesList import DIR_CLIENT_HEADER_TIMEOUT
from ...Common import DirectiveBase, TimeInterval, TimeIntervalGroup

class ClientHeaderTimeout(DirectiveBase):
    def __init__(
        self,
        time : TimeInterval | TimeIntervalGroup = TimeInterval(60),
    ):
        super().__init__(DIR_CLIENT_HEADER_TIMEOUT)
        self.add_arg(time)
