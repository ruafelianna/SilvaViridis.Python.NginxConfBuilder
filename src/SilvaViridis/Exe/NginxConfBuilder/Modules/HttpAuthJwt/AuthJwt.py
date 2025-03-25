from typing import Literal

from SilvaViridis.Python.Common.Types import NonEmptyString

from ...Common import DirectiveBase, OnOff, Variable

DIR_AUTH_JWT = "auth_jwt"

class AuthJwt(DirectiveBase):
    def __init__(
        self,
        order : int,
        realm : NonEmptyString | Literal[OnOff.off] = OnOff.off,
        token : Variable | None = None,
    ):
        super().__init__(order, DIR_AUTH_JWT)

        if isinstance(realm, OnOff):
            self.add_arg(realm)
        else:
            self.add_arg(realm)
            self.add_arg(token, "token=")
