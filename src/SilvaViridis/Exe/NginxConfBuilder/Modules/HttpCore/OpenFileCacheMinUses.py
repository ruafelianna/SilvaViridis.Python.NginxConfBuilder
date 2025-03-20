from ._DirectivesList import DIR_OPEN_FILE_CACHE_MIN_USES
from ...Common import DirectiveBase, PositiveInt

class OpenFileCacheMinUses(DirectiveBase):
    def __init__(
        self,
        quantity : PositiveInt = 1,
    ):
        super().__init__(DIR_OPEN_FILE_CACHE_MIN_USES)
        self.add_arg(quantity)
