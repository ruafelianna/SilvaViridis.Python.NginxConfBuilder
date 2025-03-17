from SilvaViridis.Python.Common import ValueWithUnit

from .SizeUnit import SizeUnit

class Size(ValueWithUnit[int, SizeUnit]):
    def __init__(
        self,
        value : int,
        unit : SizeUnit = SizeUnit.bytes,
    ):
        super().__init__(value, unit)
