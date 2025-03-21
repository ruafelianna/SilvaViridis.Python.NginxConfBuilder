from SilvaViridis.Python.Common import ValueWithUnit

from .OffsetUnit import OffsetUnit
from .Validators import NonNegativeInt

class Offset(ValueWithUnit[int, OffsetUnit]):
    def __init__(
        self,
        value : NonNegativeInt,
        unit : OffsetUnit,
    ):
        super().__init__(value, unit)
