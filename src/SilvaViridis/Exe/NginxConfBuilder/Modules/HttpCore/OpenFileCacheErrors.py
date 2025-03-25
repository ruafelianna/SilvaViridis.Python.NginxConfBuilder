from ...Common import DirectiveBase, OnOff

DIR_OPEN_FILE_CACHE_ERRORS = "open_file_cache_errors"

class OpenFileCacheErrors(DirectiveBase):
    def __init__(
        self,
        state : OnOff = OnOff.off,
    ):
        super().__init__(DIR_OPEN_FILE_CACHE_ERRORS)
        self.add_arg(state)
