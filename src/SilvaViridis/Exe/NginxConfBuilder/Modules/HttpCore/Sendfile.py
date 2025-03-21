from ._DirectivesList import DIR_SENDFILE
from ...Common import DirectiveBase, OnOff

class Sendfile(DirectiveBase):
    def __init__(
        self,
        state : OnOff = OnOff.off,
    ):
        super().__init__(DIR_SENDFILE)
        self.add_arg(state)
