from .DirectivesList import DIR_CONNECTION_POOL_SIZE
from ...Common import DirectiveBase, Size

class ConnectionPoolSize(DirectiveBase):
    def __init__(
        self,
        size : Size = Size(512),
    ):
        super().__init__(DIR_CONNECTION_POOL_SIZE)
        self.add_arg(size)

    @property
    def min_version(
        self,
    ) -> tuple[int, int, int]:
        return (0, 0, 0)
