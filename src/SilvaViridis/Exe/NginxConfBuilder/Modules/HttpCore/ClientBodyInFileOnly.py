from ._DirectivesList import (
    DIR_CLIENT_BODY_IN_FILE_ONLY,
    T_CLIENT_BODY_IN_FILE_ONLY__CLEAN,
    CLIENT_BODY_IN_FILE_ONLY__CLEAN
)

from ...Common import DirectiveBase, OnOff

class ClientBodyInFileOnly(DirectiveBase):
    def __init__(
        self,
        state : OnOff | T_CLIENT_BODY_IN_FILE_ONLY__CLEAN = OnOff.off,
    ):
        super().__init__(DIR_CLIENT_BODY_IN_FILE_ONLY)

        if isinstance(state, OnOff):
            self.add_enum_arg(state)
        else:
            self.add_arg(CLIENT_BODY_IN_FILE_ONLY__CLEAN)

    @property
    def min_version(
        self,
    ) -> tuple[int, int, int]:
        return (0, 0, 0)
