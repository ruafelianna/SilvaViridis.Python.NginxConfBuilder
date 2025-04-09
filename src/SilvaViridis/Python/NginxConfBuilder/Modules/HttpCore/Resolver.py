from SilvaViridis.Python.Common.Collections import NonEmptySequence

from ...Common import DirectiveBase, OnOff, Path, TimeInterval, TimeIntervalGroup, Zone

DIR_RESOLVER = "resolver"

class Resolver(DirectiveBase):
    def __init__(
        self,
        order : int,
        addresses : NonEmptySequence[Path],
        valid : TimeInterval | TimeIntervalGroup | None = None,
        ipv4 : OnOff | None = None,
        ipv6 : OnOff | None = None,
        status_zone : Zone | None = None,
    ):
        super().__init__(order, DIR_RESOLVER)

        for address in addresses:
            self.add_arg(address)

        self.add_arg(valid, "valid=")
        self.add_arg(ipv4, "ipv4=")
        self.add_arg(ipv6, "ipv6=")
        self.add_arg(status_zone, "status_zone=")
