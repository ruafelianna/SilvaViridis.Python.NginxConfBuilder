from .DirectivesList import DIR_CLIENT_HEADER_BUFFER_SIZE
from ...Common import DirectiveBase, Size, SizeUnit

class ClientHeaderBufferSize(DirectiveBase):
    def __init__(
        self,
        size : Size = Size(1, SizeUnit.kilobytes),
    ):
        super().__init__(DIR_CLIENT_HEADER_BUFFER_SIZE)
        self.add_arg(size)

    @property
    def min_version(
        self,
    ) -> tuple[int, int, int]:
        return (0, 0, 0)
