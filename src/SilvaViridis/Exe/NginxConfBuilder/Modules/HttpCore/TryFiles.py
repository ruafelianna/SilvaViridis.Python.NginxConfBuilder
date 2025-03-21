from typing import Annotated, Sequence

from SilvaViridis.Python.Common.Web import HttpStatus

from ._DirectivesList import DIR_TRY_FILES
from ...Common import DirectiveBase, Path
from ...Common.Validators import NonEmptySequenceValidator

FileList = Annotated[Sequence[Path], NonEmptySequenceValidator]

class TryFiles(DirectiveBase):
    def __init__(
        self,
        files : FileList,
        finish : Path | HttpStatus,
    ):
        super().__init__(DIR_TRY_FILES)

        for file in files:
            self.add_arg(file)

        if isinstance(finish, HttpStatus):
            self.add_arg(finish, "=")
        else:
            self.add_arg(finish)
