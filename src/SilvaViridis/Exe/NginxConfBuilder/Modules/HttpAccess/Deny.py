from typing import Literal

from ...Common import Access, DirectiveBase, Path

DIR_DENY = "deny"

class Deny(DirectiveBase):
    def __init__(
        self,
        state : Path | Literal[Access.all],
    ):
        super().__init__(DIR_DENY)
        self.add_arg(state)
