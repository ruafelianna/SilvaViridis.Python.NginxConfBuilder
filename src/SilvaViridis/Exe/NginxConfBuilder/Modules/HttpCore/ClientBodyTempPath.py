from annotated_types import MinLen
from typing import Annotated, Literal, Sequence

from ._DirectivesList import DIR_CLIENT_BODY_TEMP_PATH
from ...Common import DirectiveBase, Path

class ClientBodyTempPath(DirectiveBase):
    def __init__(
        self,
        path : Path = Path("client_body_temp"),
        levels : Annotated[Sequence[Literal[1, 2, 3]], MinLen(1)] | None = None,
    ):
        super().__init__(DIR_CLIENT_BODY_TEMP_PATH)
        self.add_arg(path)

        if levels is not None:
            for level in levels:
                self.add_arg(level)
