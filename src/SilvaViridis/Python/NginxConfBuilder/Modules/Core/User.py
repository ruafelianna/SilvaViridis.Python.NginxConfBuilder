from SilvaViridis.Python.Common.Text import NonEmptyString

from ...Common import DirectiveBase

DIR_USER = "user"

class User(DirectiveBase):
    def __init__(
        self,
        order : int,
        user : NonEmptyString = "nobody",
        group : NonEmptyString | None = None,
    ):
        super().__init__(order, DIR_USER)
        self.add_arg(user)
        self.add_arg(group)
