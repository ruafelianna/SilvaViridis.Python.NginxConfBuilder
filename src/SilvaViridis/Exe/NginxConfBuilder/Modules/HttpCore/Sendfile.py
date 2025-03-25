from ...Common import DirectiveBase, OnOff

DIR_SENDFILE = "sendfile"

class Sendfile(DirectiveBase):
    def __init__(
        self,
        state : OnOff = OnOff.off,
    ):
        super().__init__(DIR_SENDFILE)
        self.add_arg(state)
