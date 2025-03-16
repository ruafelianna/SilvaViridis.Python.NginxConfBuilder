from SilvaViridis.Python.Common.Enums import (
    OrderedEnum,
    OrderedEnumDictComparator,
)

from SilvaViridis.Python.Common.Interfaces import IComparable

class SizeUnit(OrderedEnum):
    bytes = ""
    kilobytes = "k"
    megabytes = "m"
    gigabytes = "g"

order : dict[SizeUnit, IComparable] = {
    SizeUnit.bytes: 0,
    SizeUnit.kilobytes: 1,
    SizeUnit.megabytes: 2,
    SizeUnit.gigabytes: 3,
}

OrderedEnumDictComparator(order)(SizeUnit)
