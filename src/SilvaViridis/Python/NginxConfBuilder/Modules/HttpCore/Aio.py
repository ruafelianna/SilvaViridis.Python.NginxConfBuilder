from typing import Literal

from ..Core import ThreadPool
from ...Common import DirectiveBase, OnOff

DIR_AIO = "aio"

class Aio(DirectiveBase):
    def __init__(
        self,
        order : int,
        state : OnOff | Literal["threads"] = OnOff.off,
        pool : ThreadPool | None = None,
    ):
        super().__init__(order, DIR_AIO)

        if isinstance(state, OnOff):
            self.add_arg(state)
        else:
            if pool is not None:
                self.add_arg(pool, "threads=", lambda p: p.name)
            else:
                self.add_arg("threads")

    @property
    def min_version(
        self,
    ) -> tuple[int, int, int]:
        return (0, 8, 11)
