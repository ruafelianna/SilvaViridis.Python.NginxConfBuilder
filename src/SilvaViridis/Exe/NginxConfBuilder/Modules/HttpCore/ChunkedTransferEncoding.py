from ...Common import DirectiveBase, OnOff

DIR_CHUNKED_TRANSFER_ENCODING = "chunked_transfer_encoding"

class ChunkedTransferEncoding(DirectiveBase):
    def __init__(
        self,
        order : int,
        state : OnOff = OnOff.on,
    ):
        super().__init__(order, DIR_CHUNKED_TRANSFER_ENCODING)
        self.add_arg(state)
