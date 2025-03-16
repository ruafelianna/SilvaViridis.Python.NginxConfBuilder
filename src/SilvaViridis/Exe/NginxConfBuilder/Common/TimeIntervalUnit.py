from SilvaViridis.Python.Common.Enums import (
    OrderedEnum,
    OrderedEnumDictComparator,
)

from SilvaViridis.Python.Common.Interfaces import IComparable

class TimeIntervalUnit(OrderedEnum):
    milliseconds = "ms"
    seconds  = "s"
    minutes = "m"
    hours = "h"
    days = "d"
    weeks = "w"
    months = "M" # 30 days
    years = "y" # 365 days

order : dict[TimeIntervalUnit, IComparable] = {
    TimeIntervalUnit.milliseconds: 0,
    TimeIntervalUnit.seconds: 1,
    TimeIntervalUnit.minutes: 2,
    TimeIntervalUnit.hours: 3,
    TimeIntervalUnit.days: 4,
    TimeIntervalUnit.weeks: 5,
    TimeIntervalUnit.months: 6,
    TimeIntervalUnit.years: 7,
}

OrderedEnumDictComparator(order)(TimeIntervalUnit)
