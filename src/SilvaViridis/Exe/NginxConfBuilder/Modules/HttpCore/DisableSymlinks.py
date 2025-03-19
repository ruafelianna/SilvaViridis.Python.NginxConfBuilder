from ._DirectivesList import (
    DIR_DISABLE_SYMLINKS,
    T_DISABLE_SYMLINKS__IF_NOT_OWNER,
    DISABLE_SYMLINKS__IF_NOT_OWNER,
)

from ...Common import DirectiveBase, OnOff, Path

class DisableSymlinks(DirectiveBase):
    def __init__(
        self,
        state : OnOff | T_DISABLE_SYMLINKS__IF_NOT_OWNER = OnOff.off,
        check_from : Path | None = None,
    ):
        super().__init__(DIR_DISABLE_SYMLINKS)

        if isinstance(state, OnOff):
            self.add_enum_arg(state)
        else:
            self.add_arg(DISABLE_SYMLINKS__IF_NOT_OWNER)

        if state != OnOff.off and check_from is not None:
            self.add_arg(check_from, "from=")

    @property
    def min_version(
        self,
    ) -> tuple[int, int, int]:
        return (1, 1, 15)
