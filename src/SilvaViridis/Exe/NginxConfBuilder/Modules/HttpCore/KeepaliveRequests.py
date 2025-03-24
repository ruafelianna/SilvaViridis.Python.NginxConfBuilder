from SilvaViridis.Python.Common.Types import PositiveInt

from ._DirectivesList import DIR_KEEPALIVE_REQUESTS
from ...Common import DirectiveBase

class KeepaliveRequests(DirectiveBase):
    def __init__(
        self,
        quantity : PositiveInt = 1000,
    ):
        super().__init__(DIR_KEEPALIVE_REQUESTS)
        self.add_arg(quantity)

    @property
    def min_version(
        self,
    ) -> tuple[int, int, int]:
        return (0, 8, 0)
