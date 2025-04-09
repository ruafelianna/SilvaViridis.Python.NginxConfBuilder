from ...Common import DirectiveBase, Size, SizeUnit

DIR_SENDFILE_MAX_CHUNK = "sendfile_max_chunk"

class SendfileMaxChunk(DirectiveBase):
    def __init__(
        self,
        order : int,
        size: Size = Size(value = 2, unit = SizeUnit.megabytes),
    ):
        super().__init__(order, DIR_SENDFILE_MAX_CHUNK)
        self.add_arg(size)
