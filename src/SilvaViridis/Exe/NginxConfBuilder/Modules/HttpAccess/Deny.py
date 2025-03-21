from typing import Literal

from ._DirectivesList import DIR_DENY
from ...Common import Access, DirectiveBase, Path

class Deny(DirectiveBase):
    def __init__(
        self,
        state : Path | Literal[Access.all],
    ):
        super().__init__(DIR_DENY)
        self.add_arg(state)
