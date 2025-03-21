from ._DirectivesList import DIR_SERVER_NAME_IN_REDIRECT
from ...Common import DirectiveBase, OnOff

class ServerNameInRedirect(DirectiveBase):
    def __init__(
        self,
        state : OnOff = OnOff.off,
    ):
        super().__init__(DIR_SERVER_NAME_IN_REDIRECT)
        self.add_arg(state)
