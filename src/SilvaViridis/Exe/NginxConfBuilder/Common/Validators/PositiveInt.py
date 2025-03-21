from beartype.vale import Is
from typing import Annotated

def _is_positive(
    x : int
) -> bool:
    return x > 0

PositiveInt = Annotated[int, Is[_is_positive]]
