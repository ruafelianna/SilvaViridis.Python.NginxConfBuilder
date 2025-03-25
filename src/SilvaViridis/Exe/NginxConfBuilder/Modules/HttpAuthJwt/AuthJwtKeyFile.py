from ...Common import DirectiveBase, Path

DIR_AUTH_JWT_KEY_FILE = "auth_jwt_key_file"

class AuthJwtKeyFile(DirectiveBase):
    def __init__(
        self,
        file : Path,
    ):
        super().__init__(DIR_AUTH_JWT_KEY_FILE)
        self.add_arg(file)

    @property
    def min_version(
        self,
    ) -> tuple[int, int, int]:
        return (1, 21, 4)
