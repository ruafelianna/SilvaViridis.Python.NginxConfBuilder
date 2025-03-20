from ._DirectivesList import DIR_REQUEST_POOL_SIZE
from ...Common import DirectiveBase, Size, SizeUnit

class RequestPoolSize(DirectiveBase):
    def __init__(
        self,
        size: Size = Size(4, SizeUnit.kilobytes),
    ):
        super().__init__(DIR_REQUEST_POOL_SIZE)
        self.add_arg(size)
