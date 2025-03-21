from beartype.vale import Is
from typing import Annotated

def _is_not_negative(
    x : int
) -> bool:
    return x >= 0

NonNegativeInt = Annotated[int, Is[_is_not_negative]]
