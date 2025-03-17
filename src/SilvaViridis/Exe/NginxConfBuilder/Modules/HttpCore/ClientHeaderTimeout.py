from ...Common import (
    BuildArgsHelper,
    DirectiveBase,
    TimeInterval,
    TimeIntervalGroup,
)

class ClientHeaderTimeout(DirectiveBase):
    def __init__(
        self,
        time : TimeInterval | TimeIntervalGroup = TimeInterval(60),
    ):
        args : list[str] = []

        BuildArgsHelper.add_time(args, time)

        super().__init__(
            "client_header_timeout",
            args,
        )

    @property
    def min_version(
        self,
    ) -> tuple[int, int, int]:
        return (0, 0, 0)
