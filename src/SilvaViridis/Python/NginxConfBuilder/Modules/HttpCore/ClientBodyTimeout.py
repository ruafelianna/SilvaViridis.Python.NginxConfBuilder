from ...Common import DirectiveBase, TimeInterval, TimeIntervalGroup

DIR_CLIENT_BODY_TIMEOUT = "client_body_timeout"

class ClientBodyTimeout(DirectiveBase):
    def __init__(
        self,
        order : int,
        time : TimeInterval | TimeIntervalGroup = TimeInterval(60),
    ):
        super().__init__(order, DIR_CLIENT_BODY_TIMEOUT)
        self.add_arg(time)
