from ...Common import DirectiveBase, OnOff

DIR_LOG_NOT_FOUND = "log_not_found"

class LogNotFound(DirectiveBase):
    def __init__(
        self,
        order : int,
        state : OnOff = OnOff.on,
    ):
        super().__init__(order, DIR_LOG_NOT_FOUND)
        self.add_arg(state)
