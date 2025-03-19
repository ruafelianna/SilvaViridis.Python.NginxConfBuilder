from typing import Literal, Sequence

from SilvaViridis.Python.Common.Web import HttpStatus

from ._DirectivesList import DIR_ERROR_PAGE
from ...Common import DirectiveBase, Path

class ErrorPage(DirectiveBase):
    def __init__(
        self,
        codes : Sequence[HttpStatus],
        uri : Path,
        response : HttpStatus | Literal["="] | None = None,
    ):
        super().__init__(DIR_ERROR_PAGE)

        if len(codes) == 0:
            ValueError("`codes` should contain at least one element")

        for code in codes:
            self.add_enum_arg(code)

        if isinstance(response, HttpStatus):
            self.add_arg(response, "=")
        elif response is not None:
            self.add_arg("=")

        self.add_arg(uri)

    @property
    def min_version(
        self,
    ) -> tuple[int, int, int]:
        return (0, 0, 0)
