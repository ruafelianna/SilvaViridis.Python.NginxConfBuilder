from ...Common import DirectiveBase, Size, SizeUnit

DIR_REQUEST_POOL_SIZE = "request_pool_size"

class RequestPoolSize(DirectiveBase):
    def __init__(
        self,
        size: Size = Size(4, SizeUnit.kilobytes),
    ):
        super().__init__(DIR_REQUEST_POOL_SIZE)
        self.add_arg(size)
