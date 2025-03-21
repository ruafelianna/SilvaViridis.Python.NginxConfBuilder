from ._DirectivesList import DIR_AUTH_BASIC_USER_FILE
from ...Common import DirectiveBase, Path

class AuthBasicUserFile(DirectiveBase):
    def __init__(
        self,
        file : Path,
    ):
        super().__init__(DIR_AUTH_BASIC_USER_FILE)
        self.add_arg(file)
