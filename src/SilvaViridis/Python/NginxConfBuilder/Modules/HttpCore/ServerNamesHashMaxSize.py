from ...Common import DirectiveBase, Size

DIR_SERVER_NAMES_HASH_MAX_SIZE = "server_names_hash_max_size"

class ServerNamesHashMaxSize(DirectiveBase):
    def __init__(
        self,
        order : int,
        size: Size = Size(512),
    ):
        super().__init__(order, DIR_SERVER_NAMES_HASH_MAX_SIZE)
        self.add_arg(size)
