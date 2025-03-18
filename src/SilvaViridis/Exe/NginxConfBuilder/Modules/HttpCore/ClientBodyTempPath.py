from typing import Literal, Sequence

from .DirectivesList import DIR_CLIENT_BODY_TEMP_PATH
from ...Common import DirectiveBase, Path

class ClientBodyTempPath(DirectiveBase):
    def __init__(
        self,
        path : Path = Path("client_body_temp"),
        levels : Sequence[Literal[1, 2, 3]] | None = None,
    ):
        super().__init__(DIR_CLIENT_BODY_TEMP_PATH)

        self.add_arg(path)

        if levels is not None:
            for level in levels:
                self.add_arg(level)

    @property
    def min_version(
        self,
    ) -> tuple[int, int, int]:
        return (0, 0, 0)
