from typing import Sequence

from .DirectivesList import DIR_KEEPALIVE_DISABLE, T_KEEPALIVE_DISABLE__BROWSER, KEEPALIVE_DISABLE__BROWSER__MSIE6
from ...Common import DirectiveBase

class KeepaliveDisable(DirectiveBase):
    def __init__(
        self,
        browsers : Sequence[T_KEEPALIVE_DISABLE__BROWSER] | None = [KEEPALIVE_DISABLE__BROWSER__MSIE6],
    ):
        super().__init__(DIR_KEEPALIVE_DISABLE)

        if browsers is None:
            self.add_arg("none")
        else:
            for browser in browsers:
                self.add_arg(browser)

    @property
    def min_version(
        self,
    ) -> tuple[int, int, int]:
        return (0, 0, 0)
