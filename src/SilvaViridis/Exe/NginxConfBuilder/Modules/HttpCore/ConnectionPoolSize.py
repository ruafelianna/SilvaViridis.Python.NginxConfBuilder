from ._DirectivesList import DIR_CONNECTION_POOL_SIZE
from ...Common import DirectiveBase, Size

class ConnectionPoolSize(DirectiveBase):
    def __init__(
        self,
        size : Size = Size(512),
    ):
        super().__init__(DIR_CONNECTION_POOL_SIZE)
        self.add_arg(size)
