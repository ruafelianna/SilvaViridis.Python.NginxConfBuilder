from ...Common import DirectiveBase, TimeInterval, TimeIntervalGroup

DIR_AUTH_DELAY = "auth_delay"

class AuthDelay(DirectiveBase):
    def __init__(
        self,
        order : int,
        time : TimeInterval | TimeIntervalGroup = TimeInterval(0),
    ):
        super().__init__(order, DIR_AUTH_DELAY)
        self.add_arg(time)

    @property
    def min_version(
        self,
    ) -> tuple[int, int, int]:
        return (1, 17, 10)
