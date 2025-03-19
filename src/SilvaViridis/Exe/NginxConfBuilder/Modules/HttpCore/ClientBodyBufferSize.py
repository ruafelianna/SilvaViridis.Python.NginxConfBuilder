from ._DirectivesList import DIR_CLIENT_BODY_BUFFER_SIZE
from ...Common import DirectiveBase, Size, SizeUnit

class ClientBodyBufferSize(DirectiveBase):
    def __init__(
        self,
        size : Size = Size(16, SizeUnit.kilobytes),
    ):
        super().__init__(DIR_CLIENT_BODY_BUFFER_SIZE)
        self.add_arg(size)

    @property
    def min_version(
        self,
    ) -> tuple[int, int, int]:
        return (0, 0, 0)
