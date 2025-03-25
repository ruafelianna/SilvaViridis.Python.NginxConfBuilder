from ...Common import DirectiveBase, OnOff

DIR_AIO_WRITE = "aio_write"

class AioWrite(DirectiveBase):
    def __init__(
        self,
        order : int,
        state : OnOff = OnOff.off,
    ):
        super().__init__(order, DIR_AIO_WRITE)
        self.add_arg(state)

    @property
    def min_version(
        self,
    ) -> tuple[int, int, int]:
        return (1, 9, 13)
