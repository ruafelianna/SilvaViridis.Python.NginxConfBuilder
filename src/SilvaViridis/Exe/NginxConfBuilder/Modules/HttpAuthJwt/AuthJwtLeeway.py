from ._DirectivesList import DIR_AUTH_JWT_LEEWAY
from ...Common import DirectiveBase, TimeInterval, TimeIntervalGroup

class AuthJwtLeeway(DirectiveBase):
    def __init__(
        self,
        time : TimeInterval | TimeIntervalGroup = TimeInterval(0),
    ):
        super().__init__(DIR_AUTH_JWT_LEEWAY)
        self.add_arg(time)

    @property
    def min_version(
        self,
    ) -> tuple[int, int, int]:
        return (1, 13, 10)
