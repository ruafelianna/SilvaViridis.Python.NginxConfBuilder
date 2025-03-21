from ._DirectivesList import DIR_TYPES_HASH_BUCKET_SIZE
from ...Common import DirectiveBase, Size

class TypesHashBucketSize(DirectiveBase):
    def __init__(
        self,
        size: Size = Size(64),
    ):
        super().__init__(DIR_TYPES_HASH_BUCKET_SIZE)
        self.add_arg(size)
