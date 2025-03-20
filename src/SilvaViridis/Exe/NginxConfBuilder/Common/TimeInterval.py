from SilvaViridis.Python.Common import ValueWithUnit

from ._ValidatorsList import NonNegativeInt
from .TimeIntervalUnit import TimeIntervalUnit

class TimeInterval(ValueWithUnit[int, TimeIntervalUnit]):
    def __init__(
        self,
        value : NonNegativeInt,
        unit : TimeIntervalUnit = TimeIntervalUnit.seconds,
    ):
        super().__init__(value, unit)
