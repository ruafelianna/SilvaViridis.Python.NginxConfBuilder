from beartype.vale import Is
from typing import Annotated

from .Size import Size

def _is_size_positive(
    size : Size,
) -> bool:
    return size.value > 0

type PositiveSize = Annotated[Size, Is[_is_size_positive]]
