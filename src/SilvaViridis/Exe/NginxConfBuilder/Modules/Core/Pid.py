from ._DirectivesList import DIR_PID
from ...Common import DirectiveBase, Path

class Pid(DirectiveBase):
    def __init__(
        self,
        file : Path = Path("logs/nginx.pid"),
    ):
        super().__init__(DIR_PID)
        self.add_arg(file)
