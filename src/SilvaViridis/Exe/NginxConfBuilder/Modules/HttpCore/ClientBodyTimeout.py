from ._DirectivesList import DIR_CLIENT_BODY_TIMEOUT
from ...Common import DirectiveBase, TimeInterval, TimeIntervalGroup

class ClientBodyTimeout(DirectiveBase):
    def __init__(
        self,
        time : TimeInterval | TimeIntervalGroup = TimeInterval(60),
    ):
        super().__init__(DIR_CLIENT_BODY_TIMEOUT)
        self.add_arg(time)

    @property
    def min_version(
        self,
    ) -> tuple[int, int, int]:
        return (0, 0, 0)
