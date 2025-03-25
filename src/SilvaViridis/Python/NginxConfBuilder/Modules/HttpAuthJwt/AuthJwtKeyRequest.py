from ...Common import DirectiveBase, Path

DIR_AUTH_JWT_KEY_REQUEST = "auth_jwt_key_request"

class AuthJwtKeyRequest(DirectiveBase):
    def __init__(
        self,
        order : int,
        uri : Path,
    ):
        super().__init__(order, DIR_AUTH_JWT_KEY_REQUEST)
        self.add_arg(uri)

    @property
    def min_version(
        self,
    ) -> tuple[int, int, int]:
        return (1, 15, 6)
