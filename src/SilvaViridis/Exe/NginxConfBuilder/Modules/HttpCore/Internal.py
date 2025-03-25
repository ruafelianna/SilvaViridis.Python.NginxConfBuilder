from ...Common import DirectiveBase

DIR_INTERNAL = "internal"

class Internal(DirectiveBase):
    def __init__(
        self,
        order : int,
    ):
        super().__init__(order, DIR_INTERNAL)
