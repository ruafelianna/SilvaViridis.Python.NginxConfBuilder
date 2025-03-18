from SilvaViridis.Python.Common.Text import StringHelper as SH

from .DirectivesList import DIR_AIO, T_AIO__THREADS, AIO__THREADS
from ...Common import DirectiveBase, OnOff

class Aio(DirectiveBase):
    def __init__(
        self,
        state : OnOff | T_AIO__THREADS = OnOff.off,
        pool : str | None = None,
    ):
        super().__init__(DIR_AIO)

        if isinstance(state, OnOff):
            self.add_enum_arg(state)
        else:
            if SH.is_not_none_and_not_whitespace(pool):
                self.add_arg(pool, f"{AIO__THREADS}=")
            else:
                self.add_arg(AIO__THREADS)

    @property
    def min_version(
        self,
    ) -> tuple[int, int, int]:
        return (0, 8, 11)
