from ._DirectivesList import DIR_MSIE_REFRESH
from ...Common import DirectiveBase, OnOff

class MsieRefresh(DirectiveBase):
    def __init__(
        self,
        state : OnOff = OnOff.on,
    ):
        super().__init__(DIR_MSIE_REFRESH)
        self.add_arg(state)
