from typing import Literal

from SilvaViridis.Python.Common.Collections import NonEmptySequence
from SilvaViridis.Python.Common.Web import HttpStatus

from ...Common import DirectiveBase, Path

DIR_ERROR_PAGE = "error_page"

class ErrorPage(DirectiveBase):
    def __init__(
        self,
        order : int,
        codes : NonEmptySequence[HttpStatus],
        uri : Path,
        response : HttpStatus | Literal["="] | None = None,
    ):
        super().__init__(order, DIR_ERROR_PAGE)

        for code in codes:
            self.add_arg(code)

        if isinstance(response, HttpStatus):
            self.add_arg(response, "=")
        elif response is not None:
            self.add_arg("=")

        self.add_arg(uri)
