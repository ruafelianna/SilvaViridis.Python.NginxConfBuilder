from ...Common import Access, DirectiveBase

DIR_SATISFY = "satisfy"

class Satisfy(DirectiveBase):
    def __init__(
        self,
        access : Access = Access.all,
    ):
        super().__init__(DIR_SATISFY)
        self.add_arg(access)
