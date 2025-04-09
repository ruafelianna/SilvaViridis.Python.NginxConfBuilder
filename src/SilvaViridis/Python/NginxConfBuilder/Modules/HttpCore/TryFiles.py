from SilvaViridis.Python.Common.Collections import NonEmptySequence
from SilvaViridis.Python.Common.Web import HttpStatus

from ...Common import DirectiveBase, Path

DIR_TRY_FILES = "try_files"

class TryFiles(DirectiveBase):
    def __init__(
        self,
        order : int,
        files : NonEmptySequence[Path],
        finish : Path | HttpStatus,
    ):
        super().__init__(order, DIR_TRY_FILES)

        for file in files:
            self.add_arg(file)

        if isinstance(finish, HttpStatus):
            self.add_arg(finish, "=")
        else:
            self.add_arg(finish)
