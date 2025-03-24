from typing import Literal

from SilvaViridis.Python.Common.Types import NonEmptySequence

from ._DirectivesList import DIR_SERVER_NAME
from ...Common import DirectiveBase, Path

class ServerName(DirectiveBase):
    def __init__(
        self,
        names : NonEmptySequence[Path | Literal[""]] = [""],
    ):
        super().__init__(DIR_SERVER_NAME)

        for name in names:
            self.add_arg("" if name == "" else name)
