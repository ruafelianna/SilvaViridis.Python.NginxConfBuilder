from SilvaViridis.Python.Common.Enums import (
    OrderedEnum,
    OrderedEnumDecorators,
)

from SilvaViridis.Python.Common.Interfaces import IComparable

class SizeUnit(OrderedEnum):
    bytes = ""
    kilobytes = "k"
    megabytes = "m"

_order : dict[SizeUnit, IComparable] = {
    SizeUnit.bytes: 0,
    SizeUnit.kilobytes: 1,
    SizeUnit.megabytes: 2,
}

OrderedEnumDecorators.DictComparator(_order)(SizeUnit)
