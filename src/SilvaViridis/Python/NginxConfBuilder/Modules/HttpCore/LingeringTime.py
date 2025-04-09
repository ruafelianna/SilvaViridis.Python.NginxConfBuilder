from ...Common import DirectiveBase, TimeInterval, TimeIntervalGroup

DIR_LINGERING_TIME = "lingering_time"

class LingeringTime(DirectiveBase):
    def __init__(
        self,
        order : int,
        time : TimeInterval | TimeIntervalGroup = TimeInterval(value = 30),
    ):
        super().__init__(order, DIR_LINGERING_TIME)
        self.add_arg(time)
