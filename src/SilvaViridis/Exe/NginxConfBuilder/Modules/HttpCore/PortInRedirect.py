from ._DirectivesList import DIR_PORT_IN_REDIRECT
from ...Common import DirectiveBase, OnOff

class PortInRedirect(DirectiveBase):
    def __init__(
        self,
        state : OnOff = OnOff.on,
    ):
        super().__init__(DIR_PORT_IN_REDIRECT)
        self.add_arg(state)
