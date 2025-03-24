from SilvaViridis.Python.Common import ValueWithUnit
from SilvaViridis.Python.Common.Types import NonNegativeInt

from .TimeIntervalUnit import TimeIntervalUnit

class TimeInterval(ValueWithUnit[int, TimeIntervalUnit]):
    def __init__(
        self,
        value : NonNegativeInt,
        unit : TimeIntervalUnit = TimeIntervalUnit.seconds,
    ):
        super().__init__(value, unit)
