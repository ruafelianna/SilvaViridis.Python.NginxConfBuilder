from ...Common import DirectiveBase, OnOff

DIR_SERVER_NAME_IN_REDIRECT = "server_name_in_redirect"

class ServerNameInRedirect(DirectiveBase):
    def __init__(
        self,
        order : int,
        state : OnOff = OnOff.off,
    ):
        super().__init__(order, DIR_SERVER_NAME_IN_REDIRECT)
        self.add_arg(state)
