from ._DirectivesList import DIR_ALIAS
from ...Common import DirectiveBase, Path

class Alias(DirectiveBase):
    def __init__(
        self,
        path : Path,
    ):
        super().__init__(DIR_ALIAS)
        self.add_arg(path)
