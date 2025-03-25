from ...Common import DirectiveBase, TimeInterval, TimeIntervalGroup

DIR_OPEN_FILE_CACHE_VALID = "open_file_cache_valid"

class OpenFileCacheValid(DirectiveBase):
    def __init__(
        self,
        time : TimeInterval | TimeIntervalGroup = TimeInterval(60),
    ):
        super().__init__(DIR_OPEN_FILE_CACHE_VALID)
        self.add_arg(time)
