from ...Common import DirectiveBase, OnOff

DIR_GZIP = "gzip"

class Gzip(DirectiveBase):
    def __init__(
        self,
        order : int,
        state : OnOff = OnOff.off,
    ):
        super().__init__(order, DIR_GZIP)
        self.add_arg(state)
