from typing import Literal

from ...Common import Access, DirectiveBase, Path

DIR_ALLOW = "allow"

class Allow(DirectiveBase):
    def __init__(
        self,
        order : int,
        state : Path | Literal[Access.all],
    ):
        super().__init__(order, DIR_ALLOW)
        self.add_arg(state)
