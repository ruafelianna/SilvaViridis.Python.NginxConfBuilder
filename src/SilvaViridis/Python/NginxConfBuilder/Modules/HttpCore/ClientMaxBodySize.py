from ...Common import DirectiveBase, Size, SizeUnit

DIR_CLIENT_MAX_BODY_SIZE = "client_max_body_size"

class ClientMaxBodySize(DirectiveBase):
    def __init__(
        self,
        order : int,
        size : Size = Size(1, SizeUnit.megabytes),
    ):
        super().__init__(order, DIR_CLIENT_MAX_BODY_SIZE)
        self.add_arg(size)
