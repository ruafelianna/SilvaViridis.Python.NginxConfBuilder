from typing import Literal

from ...Common import DirectiveBase, OnOff, Path

DIR_DISABLE_SYMLINKS = "disable_symlinks"

class DisableSymlinks(DirectiveBase):
    def __init__(
        self,
        order : int,
        state : OnOff | Literal["if_not_owner"] = OnOff.off,
        check_from : Path | None = None,
    ):
        super().__init__(order, DIR_DISABLE_SYMLINKS)
        self.add_arg(state)

        if state != OnOff.off and check_from is not None:
            self.add_arg(check_from, "from=")

    @property
    def min_version(
        self,
    ) -> tuple[int, int, int]:
        return (1, 1, 15)
