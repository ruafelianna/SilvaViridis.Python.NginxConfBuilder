from SilvaViridis.Python.Common.Numbers import PositiveInt

from ...Common import DirectiveBase, Size, SizeUnit

DIR_OUTPUT_BUFFERS = "output_buffers"

class OutputBuffers(DirectiveBase):
    def __init__(
        self,
        order : int,
        quantity : PositiveInt = 2,
        size : Size = Size(value = 32, unit = SizeUnit.kilobytes),
    ):
        super().__init__(order, DIR_OUTPUT_BUFFERS)
        self.add_arg(quantity)
        self.add_arg(size)
