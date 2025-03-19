from ._DirectivesList import DIR_AIO_WRITE
from ...Common import DirectiveBase, OnOff

class AioWrite(DirectiveBase):
    def __init__(
        self,
        state : OnOff = OnOff.off,
    ):
        super().__init__(DIR_AIO_WRITE)
        self.add_arg(state)

    @property
    def min_version(
        self,
    ) -> tuple[int, int, int]:
        return (1, 9, 13)
