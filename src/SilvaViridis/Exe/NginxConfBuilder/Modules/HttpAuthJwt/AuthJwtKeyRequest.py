from ._DirectivesList import DIR_AUTH_JWT_KEY_REQUEST
from ...Common import DirectiveBase, Path

class AuthJwtKeyRequest(DirectiveBase):
    def __init__(
        self,
        uri : Path,
    ):
        super().__init__(DIR_AUTH_JWT_KEY_REQUEST)
        self.add_arg(uri)

    @property
    def min_version(
        self,
    ) -> tuple[int, int, int]:
        return (1, 15, 6)
