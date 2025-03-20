from ._DirectivesList import DIR_OPEN_FILE_CACHE_ERRORS
from ...Common import DirectiveBase, OnOff

class OpenFileCacheErrors(DirectiveBase):
    def __init__(
        self,
        state : OnOff = OnOff.off,
    ):
        super().__init__(DIR_OPEN_FILE_CACHE_ERRORS)
        self.add_arg(state)
