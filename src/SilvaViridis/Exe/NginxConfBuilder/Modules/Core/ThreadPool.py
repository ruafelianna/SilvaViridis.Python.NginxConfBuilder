from beartype.vale import Is
from typing import Annotated

from SilvaViridis.Python.Common.Types import NonEmptyString, PositiveInt

from ._DirectivesList import DIR_THREAD_POOL
from ...Common import DirectiveBase

def _is_less_than_2_16(
    value : PositiveInt,
) -> bool:
    return value <= 65536

type PositiveInt16Plus1 = Annotated[PositiveInt, Is[_is_less_than_2_16]]

class ThreadPool(DirectiveBase):
    def __init__(
        self,
        name : NonEmptyString = "default",
        threads : PositiveInt = 32,
        max_queue : PositiveInt16Plus1 | None = 65536,
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
