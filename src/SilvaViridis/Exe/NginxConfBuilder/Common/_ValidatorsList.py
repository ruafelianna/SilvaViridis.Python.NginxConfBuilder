from beartype.vale import Is
from typing import Annotated, Sequence

from SilvaViridis.Python.Common.Text import StringHelper as SH

from .Size import Size

def _is_positive(
    x : int
) -> bool:
    return x > 0

def _is_not_negative(
    x : int
) -> bool:
    return x >= 0

def _is_not_empty_seq[T](
    seq : Sequence[T],
):
    return len(seq) > 0

def _is_size_positive(
    size : Size,
) -> bool:
    return size.value > 0

NonEmptyString = Annotated[str, Is[SH.is_not_none_and_not_whitespace]]
NonNegativeInt = Annotated[int, Is[_is_not_negative]]
PositiveInt = Annotated[int, Is[_is_positive]]
PositiveSize = Annotated[Size, Is[_is_size_positive]]

NonEmptySequenceValidator = Is[_is_not_empty_seq]
