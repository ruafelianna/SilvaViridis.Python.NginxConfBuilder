from .DirectivesList import DIR_CHUNKED_TRANSFER_ENCODING
from ...Common import DirectiveBase, OnOff

class ChunkedTransferEncoding(DirectiveBase):
    def __init__(
        self,
        state : OnOff = OnOff.on,
    ):
        super().__init__(DIR_CHUNKED_TRANSFER_ENCODING)
        self.add_enum_arg(state)

    @property
    def min_version(
        self,
    ) -> tuple[int, int, int]:
        return (0, 0, 0)
