from ...Common import DirectiveBase, OnOff

DIR_PORT_IN_REDIRECT = "port_in_redirect"

class PortInRedirect(DirectiveBase):
    def __init__(
        self,
        state : OnOff = OnOff.on,
    ):
        super().__init__(DIR_PORT_IN_REDIRECT)
        self.add_arg(state)
