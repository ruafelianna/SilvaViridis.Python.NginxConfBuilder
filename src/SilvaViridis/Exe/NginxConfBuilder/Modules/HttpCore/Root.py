from ._DirectivesList import DIR_ROOT
from ...Common import DirectiveBase, Path

class Root(DirectiveBase):
    def __init__(
        self,
        path : Path = Path("html"),
    ):
        super().__init__(DIR_ROOT)
        self.add_arg(path)
