from ...Common import DirectiveBase, Size, SizeUnit

DIR_SENDFILE_MAX_CHUNK = "sendfile_max_chunk"

class SendfileMaxChunk(DirectiveBase):
    def __init__(
        self,
        size: Size = Size(2, SizeUnit.megabytes),
    ):
        super().__init__(DIR_SENDFILE_MAX_CHUNK)
        self.add_arg(size)
