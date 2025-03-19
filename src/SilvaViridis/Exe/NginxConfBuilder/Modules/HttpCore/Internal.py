from ._DirectivesList import DIR_INTERNAL
from ...Common import DirectiveBase

class Internal(DirectiveBase):
    def __init__(
        self,
    ):
        super().__init__(DIR_INTERNAL)
