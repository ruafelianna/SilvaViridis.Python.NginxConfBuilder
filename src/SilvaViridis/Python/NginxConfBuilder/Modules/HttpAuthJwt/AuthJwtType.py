from ...Common import DirectiveBase, JSWType

DIR_AUTH_JWT_TYPE = "auth_jwt_type"

class AuthJwtType(DirectiveBase):
    def __init__(
        self,
        order : int,
        jwt_type : JSWType = JSWType.signed,
    ):
        super().__init__(order, DIR_AUTH_JWT_TYPE)
        self.add_arg(jwt_type)

    @property
    def min_version(
        self,
    ) -> tuple[int, int, int]:
        return (1, 19, 7)
