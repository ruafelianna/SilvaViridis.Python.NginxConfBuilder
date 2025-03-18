from .DirectivesList import DIR_CLIENT_BODY_IN_SINGLE_BUFFER
from ...Common import DirectiveBase, OnOff

class ClientBodyInSingleBuffer(DirectiveBase):
    def __init__(
        self,
        state : OnOff = OnOff.off,
    ):
        super().__init__(DIR_CLIENT_BODY_IN_SINGLE_BUFFER)
        self.add_enum_arg(state)

    @property
    def min_version(
        self,
    ) -> tuple[int, int, int]:
        return (0, 0, 0)
