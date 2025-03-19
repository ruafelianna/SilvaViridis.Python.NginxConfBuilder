from ._DirectivesList import DIR_CLIENT_MAX_BODY_SIZE
from ...Common import DirectiveBase, Size, SizeUnit

class ClientMaxBodySize(DirectiveBase):
    def __init__(
        self,
        size : Size = Size(1, SizeUnit.megabytes),
    ):
        super().__init__(DIR_CLIENT_MAX_BODY_SIZE)
        self.add_arg(size)
