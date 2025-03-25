from ...Common import DirectiveBase, Path

DIR_INCLUDE = "include"

class Include(DirectiveBase):
    def __init__(
        self,
        file : Path,
    ):
        super().__init__(DIR_INCLUDE)
        self.add_arg(file)
