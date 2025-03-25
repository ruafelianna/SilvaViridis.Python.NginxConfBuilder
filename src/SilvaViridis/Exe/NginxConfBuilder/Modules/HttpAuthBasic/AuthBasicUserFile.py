from ...Common import DirectiveBase, Path

DIR_AUTH_BASIC_USER_FILE = "auth_basic_user_file"

class AuthBasicUserFile(DirectiveBase):
    def __init__(
        self,
        file : Path,
    ):
        super().__init__(DIR_AUTH_BASIC_USER_FILE)
        self.add_arg(file)
