from ...Common import DirectiveBase, Size, SizeUnit

DIR_SUBREQUEST_OUTPUT_BUFFER_SIZE = "subrequest_output_buffer_size"

class SubrequestOutputBufferSize(DirectiveBase):
    def __init__(
        self,
        order : int,
        size: Size = Size(8, SizeUnit.kilobytes),
    ):
        super().__init__(order, DIR_SUBREQUEST_OUTPUT_BUFFER_SIZE)
        self.add_arg(size)

    @property
    def min_version(
        self,
    ) -> tuple[int, int, int]:
        return (1, 13, 10)
