from typing import Literal

from ._DirectivesList import DIR_SERVER_TOKENS
from ...Common import DirectiveBase, OnOff

class ServerTokens(DirectiveBase):
    def __init__(
        self,
        state : OnOff | Literal["build"] | str = OnOff.on,
    ):
        super().__init__(DIR_SERVER_TOKENS)
        self.add_arg(state)
