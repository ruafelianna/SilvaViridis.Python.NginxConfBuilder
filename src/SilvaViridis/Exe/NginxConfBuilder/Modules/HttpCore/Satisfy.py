from ._DirectivesList import DIR_SATISFY
from ...Common import Access, DirectiveBase

class Satisfy(DirectiveBase):
    def __init__(
        self,
        access : Access = Access.all,
    ):
        super().__init__(DIR_SATISFY)
        self.add_arg(access)
