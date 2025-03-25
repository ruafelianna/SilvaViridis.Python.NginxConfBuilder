from ...Common import DirectiveBase, Path

DIR_ROOT = "root"

class Root(DirectiveBase):
    def __init__(
        self,
        order : int,
        path : Path = Path("html"),
    ):
        super().__init__(order, DIR_ROOT)
        self.add_arg(path)
