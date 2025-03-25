from ...Common import DirectiveBase, Size

DIR_DIRECTIO_ALIGNMENT = "directio_alignment"

class DirectioAlignment(DirectiveBase):
    def __init__(
        self,
        size : Size = Size(512),
    ):
        super().__init__(DIR_DIRECTIO_ALIGNMENT)
        self.add_arg(size)

    @property
    def min_version(
        self,
    ) -> tuple[int, int, int]:
        return (0, 8, 11)
