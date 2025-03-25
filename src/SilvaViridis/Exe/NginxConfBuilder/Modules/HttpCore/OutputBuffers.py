from SilvaViridis.Python.Common.Types import PositiveInt

from ...Common import DirectiveBase, Size, SizeUnit

DIR_OUTPUT_BUFFERS = "output_buffers"

class OutputBuffers(DirectiveBase):
    def __init__(
        self,
        quantity : PositiveInt = 2,
        size : Size = Size(32, SizeUnit.kilobytes),
    ):
        super().__init__(DIR_OUTPUT_BUFFERS)
        self.add_arg(quantity)
        self.add_arg(size)
