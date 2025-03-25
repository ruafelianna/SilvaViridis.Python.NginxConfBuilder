from ...Common import DirectiveBase, OnOff

DIR_MSIE_REFRESH = "msie_refresh"

class MsieRefresh(DirectiveBase):
    def __init__(
        self,
        state : OnOff = OnOff.on,
    ):
        super().__init__(DIR_MSIE_REFRESH)
        self.add_arg(state)
