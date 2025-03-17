from SilvaViridis.Python.Common import ValueWithUnit

from .TimeIntervalUnit import TimeIntervalUnit

class TimeInterval(ValueWithUnit[int, TimeIntervalUnit]):
    def __init__(
        self,
        value : int,
        unit : TimeIntervalUnit = TimeIntervalUnit.seconds,
    ):
        super().__init__(value, unit)
