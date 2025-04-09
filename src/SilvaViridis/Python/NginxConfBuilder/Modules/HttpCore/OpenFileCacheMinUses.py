from SilvaViridis.Python.Common.Numbers import PositiveInt

from ...Common import DirectiveBase

DIR_OPEN_FILE_CACHE_MIN_USES = "open_file_cache_min_uses"

class OpenFileCacheMinUses(DirectiveBase):
    def __init__(
        self,
        order : int,
        quantity : PositiveInt = 1,
    ):
        super().__init__(order, DIR_OPEN_FILE_CACHE_MIN_USES)
        self.add_arg(quantity)
