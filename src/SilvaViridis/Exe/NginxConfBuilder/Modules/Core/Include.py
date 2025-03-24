from ._DirectivesList import DIR_INCLUDE
from ...Common import DirectiveBase, Path

class Include(DirectiveBase):
    def __init__(
        self,
        file : Path,
    ):
        super().__init__(DIR_INCLUDE)
        self.add_arg(file)
