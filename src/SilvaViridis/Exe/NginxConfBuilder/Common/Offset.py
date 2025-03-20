from SilvaViridis.Python.Common import ValueWithUnit

from ._ValidatorsList import NonNegativeInt
from .OffsetUnit import OffsetUnit

class Offset(ValueWithUnit[int, OffsetUnit]):
    def __init__(
        self,
        value : NonNegativeInt,
        unit : OffsetUnit,
    ):
        super().__init__(value, unit)
