from beartype.vale import Is
from typing import Annotated

from SilvaViridis.Python.Common.Types import NonEmptyString, PositiveInt

from ...Common import DirectiveBase

DIR_THREAD_POOL = "thread_pool"

def _is_less_than_2_16(
    value : PositiveInt,
) -> bool:
    return value <= 65536

type PositiveInt16Plus1 = Annotated[PositiveInt, Is[_is_less_than_2_16]]

class ThreadPool(DirectiveBase):
    def __init__(
        self,
        order : int,
        name : NonEmptyString = "default",
        threads : PositiveInt = 32,
        max_queue : PositiveInt16Plus1 | None = 65536,
    ):
        super().__init__(order, DIR_THREAD_POOL)
        self.add_arg(name)
        self.add_arg(threads, "threads=")
        self.add_arg(max_queue, "max_queue=")

    @property
    def min_version(
        self,
    ) -> tuple[int, int, int]:
        return (1, 7, 11)
