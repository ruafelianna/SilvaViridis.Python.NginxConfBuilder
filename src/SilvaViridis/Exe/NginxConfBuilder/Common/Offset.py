from SilvaViridis.Python.Common import ValueWithUnit

from .OffsetUnit import OffsetUnit

class Offset(ValueWithUnit[int, OffsetUnit]):
    def __init__(
        self,
        value : int,
        unit : OffsetUnit,
    ):
        super().__init__(value, unit)
