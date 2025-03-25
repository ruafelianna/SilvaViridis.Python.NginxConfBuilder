from ...Common import DirectiveBase, Size

DIR_VARIABLES_HASH_MAX_SIZE = "variables_hash_max_size"

class VariablesHashMaxSize(DirectiveBase):
    def __init__(
        self,
        size: Size = Size(1024),
    ):
        super().__init__(DIR_VARIABLES_HASH_MAX_SIZE)
        self.add_arg(size)
