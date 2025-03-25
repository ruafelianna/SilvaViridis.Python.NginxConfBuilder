from ...Common import DirectiveBase, Size

DIR_TYPES_HASH_MAX_SIZE = "types_hash_max_size"

class TypesHashMaxSize(DirectiveBase):
    def __init__(
        self,
        size: Size = Size(1024),
    ):
        super().__init__(DIR_TYPES_HASH_MAX_SIZE)
        self.add_arg(size)
