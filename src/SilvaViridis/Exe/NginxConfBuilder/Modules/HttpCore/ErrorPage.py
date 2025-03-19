from annotated_types import MinLen
from typing import Annotated, Literal, Sequence

from SilvaViridis.Python.Common.Web import HttpStatus

from ._DirectivesList import DIR_ERROR_PAGE
from ...Common import DirectiveBase, Path

class ErrorPage(DirectiveBase):
    def __init__(
        self,
        codes : Annotated[Sequence[HttpStatus], MinLen(1)],
        uri : Path,
        response : HttpStatus | Literal["="] | None = None,
    ):
        super().__init__(DIR_ERROR_PAGE)

        for code in codes:
            self.add_arg(code)

        if isinstance(response, HttpStatus):
            self.add_arg(response, "=")
        elif response is not None:
            self.add_arg("=")

        self.add_arg(uri)
