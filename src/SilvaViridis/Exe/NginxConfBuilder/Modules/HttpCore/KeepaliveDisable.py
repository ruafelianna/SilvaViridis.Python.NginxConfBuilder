from annotated_types import MinLen
from typing import Annotated, Literal, Sequence

from ._DirectivesList import DIR_KEEPALIVE_DISABLE
from ...Common import DirectiveBase

class KeepaliveDisable(DirectiveBase):
    def __init__(
        self,
        browsers : Annotated[Sequence[Literal["msie6", "safari"]], MinLen(1)] | None = ["msie6"],
    ):
        super().__init__(DIR_KEEPALIVE_DISABLE)

        if browsers is None:
            self.add_arg("none")
        else:
            for browser in browsers:
                self.add_arg(browser)
