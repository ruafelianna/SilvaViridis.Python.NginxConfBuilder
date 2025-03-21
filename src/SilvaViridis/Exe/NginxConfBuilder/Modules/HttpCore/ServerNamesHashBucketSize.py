from ._DirectivesList import DIR_SERVER_NAMES_HASH_BUCKET_SIZE
from ...Common import DirectiveBase, Size

class ServerNamesHashBucketSize(DirectiveBase):
    def __init__(
        self,
        size: Size = Size(64),
    ):
        super().__init__(DIR_SERVER_NAMES_HASH_BUCKET_SIZE)
        self.add_arg(size)
