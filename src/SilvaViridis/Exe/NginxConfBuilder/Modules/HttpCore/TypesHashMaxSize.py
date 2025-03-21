from ._DirectivesList import DIR_TYPES_HASH_MAX_SIZE
from ...Common import DirectiveBase, Size

class TypesHashMaxSize(DirectiveBase):
    def __init__(
        self,
        size: Size = Size(1024),
    ):
        super().__init__(DIR_TYPES_HASH_MAX_SIZE)
        self.add_arg(size)
