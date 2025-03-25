from ...Common import DirectiveBase, Path

DIR_ALIAS = "alias"

class Alias(DirectiveBase):
    def __init__(
        self,
        path : Path,
    ):
        super().__init__(DIR_ALIAS)
        self.add_arg(path)
