from ._DirectivesList import DIR_SENDFILE_MAX_CHUNK
from ...Common import DirectiveBase, Size, SizeUnit

class SendfileMaxChunk(DirectiveBase):
    def __init__(
        self,
        size: Size = Size(2, SizeUnit.megabytes),
    ):
        super().__init__(DIR_SENDFILE_MAX_CHUNK)
        self.add_arg(size)
