from SilvaViridis.Python.Common.Types import PositiveInt

from ...Common import DirectiveBase

DIR_OPEN_FILE_CACHE_MIN_USES = "open_file_cache_min_uses"

class OpenFileCacheMinUses(DirectiveBase):
    def __init__(
        self,
        quantity : PositiveInt = 1,
    ):
        super().__init__(DIR_OPEN_FILE_CACHE_MIN_USES)
        self.add_arg(quantity)
