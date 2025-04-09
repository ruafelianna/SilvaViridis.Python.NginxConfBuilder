from typing import Literal

from SilvaViridis.Python.Common.Text import NonEmptyString

from ...Common import DirectiveBase, OnOff

DIR_AUTH_BASIC = "auth_basic"

class AuthBasic(DirectiveBase):
    def __init__(
        self,
        order : int,
        realm : NonEmptyString | Literal[OnOff.off] = OnOff.off,
    ):
        super().__init__(order, DIR_AUTH_BASIC)
        self.add_arg(realm)
