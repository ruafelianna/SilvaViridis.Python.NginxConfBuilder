from ._DirectivesList import DIR_AUTH_JWT_TYPE
from ...Common import DirectiveBase, JSWType

class AuthJwtType(DirectiveBase):
    def __init__(
        self,
        jwt_type : JSWType = JSWType.signed,
    ):
        super().__init__(DIR_AUTH_JWT_TYPE)
        self.add_arg(jwt_type)

    @property
    def min_version(
        self,
    ) -> tuple[int, int, int]:
        return (1, 19, 7)
