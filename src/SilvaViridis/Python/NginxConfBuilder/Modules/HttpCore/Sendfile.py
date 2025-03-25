from ...Common import DirectiveBase, OnOff

DIR_SENDFILE = "sendfile"

class Sendfile(DirectiveBase):
    def __init__(
        self,
        order : int,
        state : OnOff = OnOff.off,
    ):
        super().__init__(order, DIR_SENDFILE)
        self.add_arg(state)
