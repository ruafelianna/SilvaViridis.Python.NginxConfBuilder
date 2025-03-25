from ...Common import DirectiveBase, Size

DIR_DIRECTIO_ALIGNMENT = "directio_alignment"

class DirectioAlignment(DirectiveBase):
    def __init__(
        self,
        order : int,
        size : Size = Size(512),
    ):
        super().__init__(order, DIR_DIRECTIO_ALIGNMENT)
        self.add_arg(size)

    @property
    def min_version(
        self,
    ) -> tuple[int, int, int]:
        return (0, 8, 11)
