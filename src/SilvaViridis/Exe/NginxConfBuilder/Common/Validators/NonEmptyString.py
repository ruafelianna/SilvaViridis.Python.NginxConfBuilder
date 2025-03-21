from beartype.vale import Is
from typing import Annotated

from SilvaViridis.Python.Common.Text import StringHelper as SH

NonEmptyString = Annotated[str, Is[SH.is_not_none_and_not_whitespace]]
