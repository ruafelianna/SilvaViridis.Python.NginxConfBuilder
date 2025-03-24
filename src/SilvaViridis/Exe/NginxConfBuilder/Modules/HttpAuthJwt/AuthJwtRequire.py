from collections.abc import Sequence
from typing import Literal

from SilvaViridis.Python.Common.Types import NonEmptyString
from SilvaViridis.Python.Common.Web import HttpStatus

from ._DirectivesList import DIR_AUTH_JWT_REQUIRE
from ...Common import DirectiveBase, Variable

class AuthJwtRequire(DirectiveBase):
    def __init__(
        self,
        variable : Variable,
        values : Sequence[NonEmptyString | Variable] = [],
        error : Literal[HttpStatus.Unauthorized, HttpStatus.Forbidden] | None = None,
    ):
        super().__init__(DIR_AUTH_JWT_REQUIRE)
        self.add_arg(variable)

        for value in values:
            self.add_arg(value)

        self.add_arg(error, "error=")

    @property
    def min_version(
        self,
    ) -> tuple[int, int, int]:
        return (1, 21, 2)
