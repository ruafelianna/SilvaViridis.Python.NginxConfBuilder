from ...Common import DirectiveBase, OnOff

DIR_SSL_PREFER_SERVER_CIPHERS = "ssl_prefer_server_ciphers"

class SslPreferServerCiphers(DirectiveBase):
    def __init__(
        self,
        order : int,
        state : OnOff = OnOff.off,
    ):
        super().__init__(order, DIR_SSL_PREFER_SERVER_CIPHERS)
        self.add_arg(state)
