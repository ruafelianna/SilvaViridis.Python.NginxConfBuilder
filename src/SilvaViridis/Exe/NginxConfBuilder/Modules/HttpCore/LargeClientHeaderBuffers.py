from annotated_types import Gt
from typing import Annotated

from ._DirectivesList import DIR_LARGE_CLIENT_HEADER_BUFFERS
from ...Common import DirectiveBase, Size, SizeUnit

class LargeClientHeaderBuffers(DirectiveBase):
    def __init__(
        self,
        number : Annotated[int, Gt(0)] = 4,
        size : Size = Size(8, SizeUnit.kilobytes),
    ):
        super().__init__(DIR_LARGE_CLIENT_HEADER_BUFFERS)
        self.add_arg(number)
        self.add_arg(size)
