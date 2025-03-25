from ...Common import DirectiveBase, OnOff

DIR_ABSOLUTE_REDIRECT = "absolute_redirect"

class AbsoluteRedirect(DirectiveBase):
    def __init__(
        self,
        order : int,
        state : OnOff = OnOff.on,
    ):
        super().__init__(order, DIR_ABSOLUTE_REDIRECT)
        self.add_arg(state)

    @property
    def min_version(
        self,
    ) -> tuple[int, int, int]:
        return (1, 11, 8)
