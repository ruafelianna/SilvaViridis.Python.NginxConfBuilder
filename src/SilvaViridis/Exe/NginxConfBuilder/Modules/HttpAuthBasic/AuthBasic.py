from typing import Literal

from SilvaViridis.Python.Common.Types import NonEmptyString

from ...Common import DirectiveBase, OnOff

DIR_AUTH_BASIC = "auth_basic"

class AuthBasic(DirectiveBase):
    def __init__(
        self,
        realm : NonEmptyString | Literal[OnOff.off] = OnOff.off,
    ):
        super().__init__(DIR_AUTH_BASIC)
        self.add_arg(realm)
