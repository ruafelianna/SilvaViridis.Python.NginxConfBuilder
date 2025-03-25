from ...Common import DirectiveBase, TimeInterval, TimeIntervalGroup

DIR_SEND_TIMEOUT = "send_timeout"

class SendTimeout(DirectiveBase):
    def __init__(
        self,
        time : TimeInterval | TimeIntervalGroup = TimeInterval(60),
    ):
        super().__init__(DIR_SEND_TIMEOUT)
        self.add_arg(time)
