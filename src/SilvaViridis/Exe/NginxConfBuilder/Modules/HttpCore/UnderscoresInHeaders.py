from ...Common import DirectiveBase, OnOff

DIR_UNDERSCORES_IN_HEADERS = "underscores_in_headers"

class UnderscoresInHeaders(DirectiveBase):
    def __init__(
        self,
        state : OnOff = OnOff.off,
    ):
        super().__init__(DIR_UNDERSCORES_IN_HEADERS)
        self.add_arg(state)
