from typing import Literal

from ...Common import DirectiveBase, OnOff

DIR_CLIENT_BODY_IN_FILE_ONLY = "client_body_in_file_only"

class ClientBodyInFileOnly(DirectiveBase):
    def __init__(
        self,
        order : int,
        state : OnOff | Literal["clean"] = OnOff.off,
    ):
        super().__init__(order, DIR_CLIENT_BODY_IN_FILE_ONLY)
        self.add_arg(state)
