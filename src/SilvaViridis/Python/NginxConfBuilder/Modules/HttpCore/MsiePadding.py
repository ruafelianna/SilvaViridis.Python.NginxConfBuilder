from ...Common import DirectiveBase, OnOff

DIR_MSIE_PADDING = "msie_padding"

class MsiePadding(DirectiveBase):
    def __init__(
        self,
        order : int,
        state : OnOff = OnOff.on,
    ):
        super().__init__(order, DIR_MSIE_PADDING)
        self.add_arg(state)
