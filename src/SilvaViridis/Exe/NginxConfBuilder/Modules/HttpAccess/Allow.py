from typing import Literal

from ._DirectivesList import DIR_ALLOW
from ...Common import Access, DirectiveBase, Path

class Allow(DirectiveBase):
    def __init__(
        self,
        state : Path | Literal[Access.all],
    ):
        super().__init__(DIR_ALLOW)
        self.add_arg(state)
