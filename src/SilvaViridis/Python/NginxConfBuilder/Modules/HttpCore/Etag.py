from ...Common import DirectiveBase, OnOff

DIR_ETAG = "etag"

class Etag(DirectiveBase):
    def __init__(
        self,
        order : int,
        state : OnOff = OnOff.on,
    ):
        super().__init__(order, DIR_ETAG)
        self.add_arg(state)

    @property
    def min_version(
        self,
    ) -> tuple[int, int, int]:
        return (1, 3, 3)
