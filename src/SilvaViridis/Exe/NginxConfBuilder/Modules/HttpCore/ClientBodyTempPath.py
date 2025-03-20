from beartype.vale import Is
from typing import Annotated, Sequence, Literal

from ._DirectivesList import DIR_CLIENT_BODY_TEMP_PATH
from ...Common import DirectiveBase, NonEmptySequenceValidator, Path

Seq123 = Sequence[Literal[1, 2, 3]]

def _is_1_2_3(
    seq : Seq123,
) -> bool:
    return all(elem in (1, 2, 3) for elem in seq)

LevelList = Annotated[Seq123, NonEmptySequenceValidator, Is[_is_1_2_3]]

class ClientBodyTempPath(DirectiveBase):
    def __init__(
        self,
        path : Path = Path("client_body_temp"),
        levels : LevelList | None = None,
    ):
        super().__init__(DIR_CLIENT_BODY_TEMP_PATH)
        self.add_arg(path)

        if levels is not None:
            for level in levels:
                self.add_arg(level)
