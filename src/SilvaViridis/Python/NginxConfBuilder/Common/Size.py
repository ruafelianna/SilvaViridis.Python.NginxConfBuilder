from pydantic import Field

from SilvaViridis.Python.Common import ValueWithUnit
from SilvaViridis.Python.Common.Numbers import NonNegativeInt

from .SizeUnit import SizeUnit

class Size(ValueWithUnit[NonNegativeInt, SizeUnit]):
    unit : SizeUnit = Field(default = SizeUnit.bytes)
