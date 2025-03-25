from ...Common import DirectiveBase, OnOff

DIR_MSIE_REFRESH = "msie_refresh"

class MsieRefresh(DirectiveBase):
    def __init__(
        self,
        order : int,
        state : OnOff = OnOff.on,
    ):
        super().__init__(order, DIR_MSIE_REFRESH)
        self.add_arg(state)
