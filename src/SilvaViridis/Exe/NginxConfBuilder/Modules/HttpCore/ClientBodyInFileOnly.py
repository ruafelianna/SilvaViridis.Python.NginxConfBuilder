from typing import Literal

from ._DirectivesList import DIR_CLIENT_BODY_IN_FILE_ONLY
from ...Common import DirectiveBase, OnOff

class ClientBodyInFileOnly(DirectiveBase):
    def __init__(
        self,
        state : OnOff | Literal["clean"] = OnOff.off,
    ):
        super().__init__(DIR_CLIENT_BODY_IN_FILE_ONLY)
        self.add_arg(state)
