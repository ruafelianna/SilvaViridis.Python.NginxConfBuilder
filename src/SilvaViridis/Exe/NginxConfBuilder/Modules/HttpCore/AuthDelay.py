from ...Common import (
    BuildArgsHelper,
    DirectiveBase,
    TimeInterval,
    TimeIntervalGroup,
)

class AuthDelay(DirectiveBase):
    def __init__(
        self,
        time : TimeInterval | TimeIntervalGroup = TimeInterval(0),
    ):
        args : list[str] = []

        BuildArgsHelper.add_time(args, time)

        super().__init__(
            "auth_delay",
            args,
        )

    @property
    def min_version(
        self,
    ) -> tuple[int, int, int]:
        return (1, 17, 10)
