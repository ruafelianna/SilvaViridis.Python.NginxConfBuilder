from ...Common import DirectiveBase, OnOff

DIR_CLIENT_BODY_IN_SINGLE_BUFFER = "client_body_in_single_buffer"

class ClientBodyInSingleBuffer(DirectiveBase):
    def __init__(
        self,
        order : int,
        state : OnOff = OnOff.off,
    ):
        super().__init__(order, DIR_CLIENT_BODY_IN_SINGLE_BUFFER)
        self.add_arg(state)
