from ...Common import DirectiveBase, Path

DIR_INCLUDE = "include"

class Include(DirectiveBase):
    def __init__(
        self,
        order : int,
        file : Path,
    ):
        super().__init__(order, DIR_INCLUDE)
        self.add_arg(file)
