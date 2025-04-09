from typing import Literal

from SilvaViridis.Python.Common.Text import NonEmptyString

from ...Common import DirectiveBase, GzipCompressionLevel, OnOff, Path, Size, TimeInterval, TimeIntervalGroup, Variable

DIR_ACCESS_LOG = "access_log"

class AccessLog(DirectiveBase):
    def __init__(
        self,
        order : int,
        path : Path | Literal[OnOff.off] = Path("logs/access.log"),
        format : NonEmptyString | None = "combined",
        buffer : Size | None = None,
        gzip : Literal[True] | GzipCompressionLevel | None = None,
        flush : TimeInterval | TimeIntervalGroup | None = None,
        condition : Variable | None = None,
    ):
        super().__init__(order, DIR_ACCESS_LOG)
        self.add_arg(path)

        if format is not None:
            self.add_arg(format)
            self.add_arg(buffer, "buffer=")

            if gzip == True:
                self.add_arg(gzip, "gzip")
            else:
                self.add_arg(gzip, "gzip=")

            self.add_arg(flush, "flush=")
            self.add_arg(condition, "if=")
