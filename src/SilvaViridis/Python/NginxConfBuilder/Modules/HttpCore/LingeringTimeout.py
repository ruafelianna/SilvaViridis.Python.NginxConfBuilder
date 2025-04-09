from ...Common import DirectiveBase, TimeInterval, TimeIntervalGroup

DIR_LINGERING_TIMEOUT = "lingering_timeout"

class LingeringTimeout(DirectiveBase):
    def __init__(
        self,
        order : int,
        time : TimeInterval | TimeIntervalGroup = TimeInterval(value = 5),
    ):
        super().__init__(order, DIR_LINGERING_TIMEOUT)
        self.add_arg(time)
