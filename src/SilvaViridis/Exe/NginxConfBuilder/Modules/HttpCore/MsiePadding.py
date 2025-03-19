from ._DirectivesList import DIR_MSIE_PADDING
from ...Common import DirectiveBase, OnOff

class MsiePadding(DirectiveBase):
    def __init__(
        self,
        state : OnOff = OnOff.on,
    ):
        super().__init__(DIR_MSIE_PADDING)
        self.add_arg(state)
