from ._DirectivesList import DIR_SERVER_NAMES_HASH_MAX_SIZE
from ...Common import DirectiveBase, Size

class ServerNamesHashMaxSize(DirectiveBase):
    def __init__(
        self,
        size: Size = Size(512),
    ):
        super().__init__(DIR_SERVER_NAMES_HASH_MAX_SIZE)
        self.add_arg(size)
