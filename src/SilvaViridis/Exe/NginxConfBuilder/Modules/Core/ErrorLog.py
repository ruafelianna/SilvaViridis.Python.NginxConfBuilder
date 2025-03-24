from ._DirectivesList import DIR_ERROR_LOG
from ...Common import DirectiveBase, LogLevel, Path

class ErrorLog(DirectiveBase):
    def __init__(
        self,
        file : Path = Path("logs/error.log"),
        level : LogLevel | None = LogLevel.error,
    ):
        super().__init__(DIR_ERROR_LOG)
        self.add_arg(file)
        self.add_arg(level)
