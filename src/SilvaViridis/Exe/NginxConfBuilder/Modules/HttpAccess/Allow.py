from typing import Literal

from ...Common import Access, DirectiveBase, Path

DIR_ALLOW = "allow"

class Allow(DirectiveBase):
    def __init__(
        self,
        state : Path | Literal[Access.all],
    ):
        super().__init__(DIR_ALLOW)
        self.add_arg(state)
