from annotated_types import Gt, Le
from typing import Annotated

from SilvaViridis.Python.Common.Text import StringHelper as SH

from ._DirectivesList import DIR_THREAD_POOL
from ...Common import DirectiveBase

class ThreadPool(DirectiveBase):
    def __init__(
        self,
        name : str = "default",
        threads : Annotated[int, Gt(0)] = 32,
        max_queue : Annotated[int, Gt(0), Le(2**16)] | None = 2**16,
    ):
        if SH.is_none_or_whitespace(name):
            raise ValueError("`name` cannot be empty")

        super().__init__(DIR_THREAD_POOL)
        self.add_arg(name)
        self.add_arg(threads, "threads=")
        self.add_arg(max_queue, "max_queue=")

    @property
    def min_version(
        self,
    ) -> tuple[int, int, int]:
        return (1, 7, 11)
