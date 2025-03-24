from SilvaViridis.Python.Common.Types import NonEmptyString

from ._DirectivesList import DIR_USER
from ...Common import DirectiveBase

class User(DirectiveBase):
    def __init__(
        self,
        user : NonEmptyString = "nobody",
        group : NonEmptyString | None = None,
    ):
        super().__init__(DIR_USER)
        self.add_arg(user)
        self.add_arg(group)
