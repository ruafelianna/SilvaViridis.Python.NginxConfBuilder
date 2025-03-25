from ...Common import DirectiveBase, Path

DIR_PID = "pid"

class Pid(DirectiveBase):
    def __init__(
        self,
        order : int,
        file : Path = Path("logs/nginx.pid"),
    ):
        super().__init__(order, DIR_PID)
        self.add_arg(file)
