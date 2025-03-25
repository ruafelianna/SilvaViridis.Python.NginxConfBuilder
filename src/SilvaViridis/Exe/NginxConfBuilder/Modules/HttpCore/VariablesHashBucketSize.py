from ...Common import DirectiveBase, Size

DIR_VARIABLES_HASH_BUCKET_SIZE = "variables_hash_bucket_size"

class VariablesHashBucketSize(DirectiveBase):
    def __init__(
        self,
        size: Size = Size(64),
    ):
        super().__init__(DIR_VARIABLES_HASH_BUCKET_SIZE)
        self.add_arg(size)
