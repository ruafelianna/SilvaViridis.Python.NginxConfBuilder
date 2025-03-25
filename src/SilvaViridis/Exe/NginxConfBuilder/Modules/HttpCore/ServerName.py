from typing import Literal

from SilvaViridis.Python.Common.Types import NonEmptySequence

from ...Common import DirectiveBase, Path

DIR_SERVER_NAME = "server_name"

class ServerName(DirectiveBase):
    def __init__(
        self,
        names : NonEmptySequence[Path | Literal[""]] = [""],
    ):
        super().__init__(DIR_SERVER_NAME)

        for name in names:
            self.add_arg("" if name == "" else name)
