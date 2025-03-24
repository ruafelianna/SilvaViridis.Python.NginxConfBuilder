from typing import Literal

from SilvaViridis.Python.Common.Types import NonEmptySequence

from ._DirectivesList import DIR_KEEPALIVE_DISABLE
from ...Common import DirectiveBase

class KeepaliveDisable(DirectiveBase):
    def __init__(
        self,
        browsers : NonEmptySequence[Literal["msie6", "safari"]] | None = ["msie6"],
    ):
        super().__init__(DIR_KEEPALIVE_DISABLE)

        if browsers is None:
            self.add_arg("none")
        else:
            for browser in browsers:
                self.add_arg(browser)
