from ...Common import DirectiveBase, OnOff

DIR_RECURSIVE_ERROR_PAGES = "recursive_error_pages"

class RecursiveErrorPages(DirectiveBase):
    def __init__(
        self,
        state : OnOff = OnOff.off,
    ):
        super().__init__(DIR_RECURSIVE_ERROR_PAGES)
        self.add_arg(state)
