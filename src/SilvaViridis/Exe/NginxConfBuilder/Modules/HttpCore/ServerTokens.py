from typing import Literal

from ...Common import DirectiveBase, OnOff

DIR_SERVER_TOKENS = "server_tokens"

class ServerTokens(DirectiveBase):
    def __init__(
        self,
        order : int,
        state : OnOff | Literal["build"] | str = OnOff.on,
    ):
        super().__init__(order, DIR_SERVER_TOKENS)
        self.add_arg(state)
