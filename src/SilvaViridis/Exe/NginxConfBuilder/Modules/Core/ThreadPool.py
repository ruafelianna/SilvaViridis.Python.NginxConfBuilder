from beartype.vale import Is
from typing import Annotated

from ._DirectivesList import DIR_THREAD_POOL
from ...Common import DirectiveBase
from ...Common.Validators import NonEmptyString, PositiveInt

def _is_less_than_2_16(
    value : PositiveInt,
) -> bool:
    return value <= 2**16

PositiveInt2BytesPlusOne = Annotated[PositiveInt, Is[_is_less_than_2_16]]

class ThreadPool(DirectiveBase):
    def __init__(
        self,
        name : NonEmptyString = "default",
        threads : PositiveInt = 32,
        max_queue : PositiveInt2BytesPlusOne | None = 2**16,
    ):
        super().__init__(DIR_THREAD_POOL)
        self.add_arg(name)
        self.add_arg(threads, "threads=")
        self.add_arg(max_queue, "max_queue=")

    @property
    def min_version(
        self,
    ) -> tuple[int, int, int]:
        return (1, 7, 11)
