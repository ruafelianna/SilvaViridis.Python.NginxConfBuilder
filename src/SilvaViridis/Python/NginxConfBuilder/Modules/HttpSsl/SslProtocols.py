from ...Common import DirectiveBase

DIR_SSL_PROTOCOLS = "ssl_protocols"

class SslProtocols(DirectiveBase):
    def __init__(
        self,
        order : int,
        SSLv2 : bool = False,
        SSLv3 : bool = False,
        TLSv1 : bool = False,
        TLSv1_1 : bool = False,
        TLSv1_2 : bool = True,
        TLSv1_3 : bool = True,
    ):
        super().__init__(order, DIR_SSL_PROTOCOLS)
        self.add_arg(SSLv2, "SSLv2")
        self.add_arg(SSLv3, "SSLv3")
        self.add_arg(TLSv1, "TLSv1")
        self.add_arg(TLSv1_1, "TLSv1.1")
        self.add_arg(TLSv1_2, "TLSv1.2")
        self.add_arg(TLSv1_3, "TLSv1.3")
