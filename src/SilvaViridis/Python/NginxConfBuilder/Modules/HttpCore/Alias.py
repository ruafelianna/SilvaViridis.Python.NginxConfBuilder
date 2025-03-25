from ...Common import DirectiveBase, Path

DIR_ALIAS = "alias"

class Alias(DirectiveBase):
    def __init__(
        self,
        order : int,
        path : Path,
    ):
        super().__init__(order, DIR_ALIAS)
        self.add_arg(path)
