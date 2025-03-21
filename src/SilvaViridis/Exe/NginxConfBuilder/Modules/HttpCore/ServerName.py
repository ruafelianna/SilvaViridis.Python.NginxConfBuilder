from typing import Annotated, Literal, Sequence

from ._DirectivesList import DIR_SERVER_NAME
from ...Common import DirectiveBase, Path
from ...Common.Validators import NonEmptySequenceValidator

ServerNameList = Annotated[Sequence[Path | Literal[""]], NonEmptySequenceValidator]

class ServerName(DirectiveBase):
    def __init__(
        self,
        names : ServerNameList = [""],
    ):
        super().__init__(DIR_SERVER_NAME)

        for name in names:
            self.add_arg("" if name == "" else name)
