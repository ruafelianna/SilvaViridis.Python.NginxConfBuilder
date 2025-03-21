from ._DirectivesList import DIR_SUBREQUEST_OUTPUT_BUFFER_SIZE
from ...Common import DirectiveBase, Size, SizeUnit

class SubrequestOutputBufferSize(DirectiveBase):
    def __init__(
        self,
        size: Size = Size(8, SizeUnit.kilobytes),
    ):
        super().__init__(DIR_SUBREQUEST_OUTPUT_BUFFER_SIZE)
        self.add_arg(size)

    @property
    def min_version(
        self,
    ) -> tuple[int, int, int]:
        return (1, 13, 10)
