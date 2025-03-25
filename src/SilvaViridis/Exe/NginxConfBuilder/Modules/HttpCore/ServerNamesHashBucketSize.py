from ...Common import DirectiveBase, Size

DIR_SERVER_NAMES_HASH_BUCKET_SIZE = "server_names_hash_bucket_size"

class ServerNamesHashBucketSize(DirectiveBase):
    def __init__(
        self,
        size: Size = Size(64),
    ):
        super().__init__(DIR_SERVER_NAMES_HASH_BUCKET_SIZE)
        self.add_arg(size)
