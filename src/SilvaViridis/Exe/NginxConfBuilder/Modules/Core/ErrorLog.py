from ...Common import DirectiveBase, LogLevel, Path

DIR_ERROR_LOG = "error_log"

class ErrorLog(DirectiveBase):
    def __init__(
        self,
        file : Path = Path("logs/error.log"),
        level : LogLevel | None = LogLevel.error,
    ):
        super().__init__(DIR_ERROR_LOG)
        self.add_arg(file)
        self.add_arg(level)
