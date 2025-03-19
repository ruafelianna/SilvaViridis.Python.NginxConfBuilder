from ._DirectivesList import DIR_CLIENT_BODY_IN_SINGLE_BUFFER
from ...Common import DirectiveBase, OnOff

class ClientBodyInSingleBuffer(DirectiveBase):
    def __init__(
        self,
        state : OnOff = OnOff.off,
    ):
        super().__init__(DIR_CLIENT_BODY_IN_SINGLE_BUFFER)
        self.add_arg(state)
