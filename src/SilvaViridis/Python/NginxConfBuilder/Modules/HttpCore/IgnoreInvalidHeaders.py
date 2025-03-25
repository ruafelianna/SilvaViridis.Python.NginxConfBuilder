from ...Common import DirectiveBase, OnOff

DIR_IGNORE_INVALID_HEADERS = "ignore_invalid_headers"

class IgnoreInvalidHeaders(DirectiveBase):
    def __init__(
        self,
        order : int,
        state : OnOff = OnOff.on,
    ):
        super().__init__(order, DIR_IGNORE_INVALID_HEADERS)
        self.add_arg(state)
