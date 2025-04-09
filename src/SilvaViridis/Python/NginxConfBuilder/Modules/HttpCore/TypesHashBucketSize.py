from ...Common import DirectiveBase, Size

DIR_TYPES_HASH_BUCKET_SIZE = "types_hash_bucket_size"

class TypesHashBucketSize(DirectiveBase):
    def __init__(
        self,
        order : int,
        size: Size = Size(value = 64),
    ):
        super().__init__(order, DIR_TYPES_HASH_BUCKET_SIZE)
        self.add_arg(size)
