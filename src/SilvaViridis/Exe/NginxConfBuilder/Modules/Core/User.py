from SilvaViridis.Python.Common.Types import NonEmptyString

from ...Common import DirectiveBase

DIR_USER = "user"

class User(DirectiveBase):
    def __init__(
        self,
        user : NonEmptyString = "nobody",
        group : NonEmptyString | None = None,
    ):
        super().__init__(DIR_USER)
        self.add_arg(user)
        self.add_arg(group)
