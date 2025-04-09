from pydantic import Field

from SilvaViridis.Python.Common import ValueWithUnit
from SilvaViridis.Python.Common.Numbers import NonNegativeInt

from .TimeIntervalUnit import TimeIntervalUnit

class TimeInterval(ValueWithUnit[NonNegativeInt, TimeIntervalUnit]):
    unit : TimeIntervalUnit = Field(default = TimeIntervalUnit.seconds)
