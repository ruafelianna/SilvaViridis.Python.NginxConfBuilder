from ...Common import DirectiveBase, TimeInterval, TimeIntervalGroup

DIR_AUTH_JWT_KEY_CACHE = "auth_jwt_key_cache"

class AuthJwtKeyCache(DirectiveBase):
    def __init__(
        self,
        time : TimeInterval | TimeIntervalGroup = TimeInterval(0),
    ):
        super().__init__(DIR_AUTH_JWT_KEY_CACHE)
        self.add_arg(time)

    @property
    def min_version(
        self,
    ) -> tuple[int, int, int]:
        return (1, 21, 4)
