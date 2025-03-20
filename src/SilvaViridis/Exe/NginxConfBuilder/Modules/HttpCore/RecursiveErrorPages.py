from ._DirectivesList import DIR_RECURSIVE_ERROR_PAGES
from ...Common import DirectiveBase, OnOff

class RecursiveErrorPages(DirectiveBase):
    def __init__(
        self,
        state : OnOff = OnOff.off,
    ):
        super().__init__(DIR_RECURSIVE_ERROR_PAGES)
        self.add_arg(state)
