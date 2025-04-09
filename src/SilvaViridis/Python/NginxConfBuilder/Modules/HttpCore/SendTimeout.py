from ...Common import DirectiveBase, TimeInterval, TimeIntervalGroup

DIR_SEND_TIMEOUT = "send_timeout"

class SendTimeout(DirectiveBase):
    def __init__(
        self,
        order : int,
        time : TimeInterval | TimeIntervalGroup = TimeInterval(value = 60),
    ):
        super().__init__(order, DIR_SEND_TIMEOUT)
        self.add_arg(time)
