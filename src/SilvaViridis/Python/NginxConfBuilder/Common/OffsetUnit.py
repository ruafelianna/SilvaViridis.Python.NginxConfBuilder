from SilvaViridis.Python.Common.Enums import (
    OrderedEnum,
    OrderedEnumDecorators,
)

from SilvaViridis.Python.Common.Interfaces import IComparable

class OffsetUnit(OrderedEnum):
    bytes = ""
    kilobytes = "k"
    megabytes = "m"
    gigabytes = "g"

_order : dict[OffsetUnit, IComparable] = {
    OffsetUnit.bytes: 0,
    OffsetUnit.kilobytes: 1,
    OffsetUnit.megabytes: 2,
    OffsetUnit.gigabytes: 3,
}

OrderedEnumDecorators.DictComparator(_order)(OffsetUnit)
