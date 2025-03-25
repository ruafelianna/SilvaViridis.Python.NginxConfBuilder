from typing import Literal

from SilvaViridis.Python.Common.Types import NonEmptySequence

from ...Common import DirectiveBase

DIR_KEEPALIVE_DISABLE = "keepalive_disable"

class KeepaliveDisable(DirectiveBase):
    def __init__(
        self,
        order : int,
        browsers : NonEmptySequence[Literal["msie6", "safari"]] | None = ["msie6"],
    ):
        super().__init__(order, DIR_KEEPALIVE_DISABLE)

        if browsers is None:
            self.add_arg("none")
        else:
            for browser in browsers:
                self.add_arg(browser)
