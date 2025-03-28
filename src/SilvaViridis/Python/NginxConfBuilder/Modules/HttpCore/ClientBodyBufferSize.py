from ...Common import DirectiveBase, Size, SizeUnit

DIR_CLIENT_BODY_BUFFER_SIZE = "client_body_buffer_size"

class ClientBodyBufferSize(DirectiveBase):
    def __init__(
        self,
        order : int,
        size : Size = Size(16, SizeUnit.kilobytes),
    ):
        super().__init__(order, DIR_CLIENT_BODY_BUFFER_SIZE)
        self.add_arg(size)
