from ...Common import DirectiveBase, Size, SizeUnit

DIR_CLIENT_HEADER_BUFFER_SIZE = "client_header_buffer_size"

class ClientHeaderBufferSize(DirectiveBase):
    def __init__(
        self,
        order : int,
        size : Size = Size(1, SizeUnit.kilobytes),
    ):
        super().__init__(order, DIR_CLIENT_HEADER_BUFFER_SIZE)
        self.add_arg(size)
