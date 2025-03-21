from typing import Annotated, Literal, Sequence

from ._DirectivesList import DIR_KEEPALIVE_DISABLE
from ...Common import DirectiveBase
from ...Common.Validators import NonEmptySequenceValidator

BrowserList = Annotated[Sequence[Literal["msie6", "safari"]], NonEmptySequenceValidator]

class KeepaliveDisable(DirectiveBase):
    def __init__(
        self,
        browsers : BrowserList | None = ["msie6"],
    ):
        super().__init__(DIR_KEEPALIVE_DISABLE)

        if browsers is None:
            self.add_arg("none")
        else:
            for browser in browsers:
                self.add_arg(browser)
