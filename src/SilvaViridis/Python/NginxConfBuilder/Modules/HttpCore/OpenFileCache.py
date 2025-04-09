from typing import Literal

from SilvaViridis.Python.Common.Numbers import PositiveInt

from ...Common import DirectiveBase, OnOff, TimeInterval, TimeIntervalGroup

DIR_OPEN_FILE_CACHE = "open_file_cache"

class OpenFileCache(DirectiveBase):
    def __init__(
        self,
        order : int,
        state : Literal[OnOff.off] | PositiveInt = OnOff.off,
        inactive : TimeInterval | TimeIntervalGroup | None = None,
    ):
        super().__init__(order, DIR_OPEN_FILE_CACHE)

        if state == OnOff.off:
            self.add_arg(state)
        else:
            self.add_arg(state, "max=")
            self.add_arg(TimeInterval(value = 60) if inactive is None else inactive)
