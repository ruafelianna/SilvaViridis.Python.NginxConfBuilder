from SilvaViridis.Python.Common import ValueWithUnit
from SilvaViridis.Python.Common.Types import NonNegativeInt

from .SizeUnit import SizeUnit

class Size(ValueWithUnit[NonNegativeInt, SizeUnit]):
    def __init__(
        self,
        value : NonNegativeInt,
        unit : SizeUnit = SizeUnit.bytes,
    ):
        super().__init__(value, unit)
