from SilvaViridis.Python.Common import ValueWithUnit

from .SizeUnit import SizeUnit
from .Validators import NonNegativeInt

class Size(ValueWithUnit[NonNegativeInt, SizeUnit]):
    def __init__(
        self,
        value : NonNegativeInt,
        unit : SizeUnit = SizeUnit.bytes,
    ):
        super().__init__(value, unit)
