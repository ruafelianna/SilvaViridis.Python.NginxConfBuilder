from SilvaViridis.Python.Common.Types import PositiveInt

from ...Common import DirectiveBase, Size, SizeUnit

DIR_LARGE_CLIENT_HEADER_BUFFERS = "large_client_header_buffers"

class LargeClientHeaderBuffers(DirectiveBase):
    def __init__(
        self,
        order : int,
        number : PositiveInt = 4,
        size : Size = Size(8, SizeUnit.kilobytes),
    ):
        super().__init__(order, DIR_LARGE_CLIENT_HEADER_BUFFERS)
        self.add_arg(number)
        self.add_arg(size)
