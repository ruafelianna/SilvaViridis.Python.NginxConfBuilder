from SilvaViridis.Python.Common import ValueWithUnit

from .TimeIntervalUnit import TimeIntervalUnit
from .Validators import NonNegativeInt

class TimeInterval(ValueWithUnit[int, TimeIntervalUnit]):
    def __init__(
        self,
        value : NonNegativeInt,
        unit : TimeIntervalUnit = TimeIntervalUnit.seconds,
    ):
        super().__init__(value, unit)
