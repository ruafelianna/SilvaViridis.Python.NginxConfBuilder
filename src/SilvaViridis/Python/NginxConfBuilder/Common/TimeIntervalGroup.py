from collections.abc import Sequence

from SilvaViridis.Python.Common.Numbers import NonNegativeInt

from .TimeInterval import TimeInterval
from .TimeIntervalUnit import TimeIntervalUnit

class TimeIntervalGroup:
    def __init__(
        self,
        intervals : Sequence[TimeInterval] = [],
    ):
        grouped : dict[TimeIntervalUnit, list[NonNegativeInt]] = {}

        for interval in intervals:
            if not interval.unit in grouped:
                grouped[interval.unit] = []
            grouped[interval.unit].append(interval.value)

        self.intervals = sorted([TimeInterval(value = sum(values), unit = unit) for unit, values in grouped.items()], reverse = True)

    def __str__(
        self,
    ) -> str:
        return " ".join((str(interval) for interval in self.intervals))
