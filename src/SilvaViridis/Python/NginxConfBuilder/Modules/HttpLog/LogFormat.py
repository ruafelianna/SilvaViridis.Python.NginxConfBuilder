from typing import Literal

from SilvaViridis.Python.Common.Types import NonEmptyString, NonEmptySequence

from ...Common import DirectiveBase

DIR_LOG_FORMAT = "log_format"

class LogFormat(DirectiveBase):
    def __init__(
        self,
        order : int,
        name : NonEmptyString = "combined",
        escape : Literal["default", "json", "none"] | None = None,
        strings : NonEmptySequence[NonEmptyString] = ["..."],
    ):
        super().__init__(order, DIR_LOG_FORMAT)
        self.add_arg(name)
        self.add_arg(escape, "escape=")

        for string in strings:
            self.add_arg(string)
