from ._DirectivesList import DIR_VARIABLES_HASH_BUCKET_SIZE
from ...Common import DirectiveBase, Size

class VariablesHashBucketSize(DirectiveBase):
    def __init__(
        self,
        size: Size = Size(64),
    ):
        super().__init__(DIR_VARIABLES_HASH_BUCKET_SIZE)
        self.add_arg(size)
