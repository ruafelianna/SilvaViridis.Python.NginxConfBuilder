from SilvaViridis.Python.Common.Types import NonEmptySequence
from SilvaViridis.Python.Common.Web import HttpStatus

from ...Common import DirectiveBase, Path

DIR_TRY_FILES = "try_files"

class TryFiles(DirectiveBase):
    def __init__(
        self,
        files : NonEmptySequence[Path],
        finish : Path | HttpStatus,
    ):
        super().__init__(DIR_TRY_FILES)

        for file in files:
            self.add_arg(file)

        if isinstance(finish, HttpStatus):
            self.add_arg(finish, "=")
        else:
            self.add_arg(finish)
