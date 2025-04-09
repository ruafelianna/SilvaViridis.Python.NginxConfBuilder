from typing import Literal

from SilvaViridis.Python.Common.Numbers import PositiveInt, UInt16
from SilvaViridis.Python.Common.Text import StringHelper as SH

from ...Common import DirectiveBase, OnOff, Path, Size, TimeInterval, TimeIntervalGroup

DIR_LISTEN = "listen"

type KeepIdle = TimeInterval | TimeIntervalGroup | None
type KeepIntvl = TimeInterval | TimeIntervalGroup | None
type KeepCnt = int | None

class Listen(DirectiveBase):
    def __init__(
        self,
        order : int,
        address : Path | None = None,
        port : UInt16 | None = None,
        unix_socket : Path | None = None,
        default_server : bool = False,
        ssl : bool = False,
        http2 : bool = False,
        quic : bool = False,
        proxy_protocol : bool = False,
        setfib : int | None = None,
        fastopen : PositiveInt | None = None,
        backlog : PositiveInt | None = None,
        rcvbuf : Size | None = None,
        sndbuf : Size | None = None,
        accept_filter : Literal["dataready", "httpready"] | None = None,
        deferred : bool = False,
        bind : bool = False,
        ipv6only : OnOff | None = None,
        reuseport : bool = False,
        so_keepalive : OnOff | tuple[KeepIdle, KeepIntvl, KeepCnt] | None = None,
    ):
        super().__init__(order, DIR_LISTEN)

        if unix_socket is not None and (address is not None or port is not None):
            raise ValueError("`unix_socket` cannot be combined with `address` or `port`")

        if unix_socket is not None and (setfib is not None or fastopen is not None or ipv6only is not None or reuseport):
            raise ValueError("`unix_socket` cannot be combined with `setfib`, `fastopen`, `ipv6only` or `reuseport`")

        if http2 and quic:
            raise ValueError("`http2` and `quic` cannot be combined")

        if isinstance(so_keepalive, tuple) and all((item is None for item in so_keepalive)):
            raise ValueError("`keepidle`, `keepintvl` or `keepcnt` should be set")

        if unix_socket is None and address is None and port is None:
            address = Path("*")
            port = 80

        if address is not None and port is not None:
            self.add_arg(f"{address}:{port}")
        else:
            self.add_arg(address)
            self.add_arg(port)
            self.add_arg(unix_socket)

        self.add_arg(default_server, "default_server")
        self.add_arg(ssl, "ssl")
        self.add_arg(http2, "http2")
        self.add_arg(quic, "quic")
        self.add_arg(proxy_protocol, "proxy_protocol")
        self.add_arg(setfib, "setfib=")
        self.add_arg(fastopen, "fastopen=")
        self.add_arg(backlog, "backlog=")
        self.add_arg(rcvbuf, "rcvbuf=")
        self.add_arg(sndbuf, "sndbuf=")
        self.add_arg(accept_filter, "accept_filter=")
        self.add_arg(deferred, "deferred")
        self.add_arg(bind, "bind")
        self.add_arg(ipv6only, "ipv6only=")
        self.add_arg(reuseport, "reuseport")

        if isinstance(so_keepalive, OnOff):
            self.add_arg(so_keepalive, "so_keepalive=")
        elif so_keepalive is not None:
            keepidle, keepintvl, keepcnt = so_keepalive
            self.add_arg(
                f"{SH.to_str_empty_if_none(keepidle)}:{SH.to_str_empty_if_none(keepintvl)}:{SH.to_str_empty_if_none(keepcnt)}",
                "so_keepalive=",
            )
