from ...Common import DirectiveBase, TimeInterval, TimeIntervalGroup

DIR_AUTH_JWT_LEEWAY = "auth_jwt_leeway"

class AuthJwtLeeway(DirectiveBase):
    def __init__(
        self,
        order : int,
        time : TimeInterval | TimeIntervalGroup = TimeInterval(value = 0),
    ):
        super().__init__(order, DIR_AUTH_JWT_LEEWAY)
        self.add_arg(time)

    @property
    def min_version(
        self,
    ) -> tuple[int, int, int]:
        return (1, 13, 10)
