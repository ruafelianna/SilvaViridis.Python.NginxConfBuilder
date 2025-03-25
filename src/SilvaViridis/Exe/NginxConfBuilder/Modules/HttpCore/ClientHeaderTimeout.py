from ...Common import DirectiveBase, TimeInterval, TimeIntervalGroup

DIR_CLIENT_HEADER_TIMEOUT = "client_header_timeout"

class ClientHeaderTimeout(DirectiveBase):
    def __init__(
        self,
        order : int,
        time : TimeInterval | TimeIntervalGroup = TimeInterval(60),
    ):
        super().__init__(order, DIR_CLIENT_HEADER_TIMEOUT)
        self.add_arg(time)
