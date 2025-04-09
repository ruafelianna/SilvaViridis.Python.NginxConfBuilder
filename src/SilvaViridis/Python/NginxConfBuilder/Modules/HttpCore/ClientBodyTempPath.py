from beartype.vale import Is
from typing import Annotated, Literal

from SilvaViridis.Python.Common.Collections import NonEmptySequence

from ...Common import DirectiveBase, Path

DIR_CLIENT_BODY_TEMP_PATH = "client_body_temp_path"

type NonEmpty123Sequence = NonEmptySequence[Literal[1, 2, 3]]

def _is_1_2_3(
    seq : NonEmpty123Sequence,
) -> bool:
    return all(elem in (1, 2, 3) for elem in seq)

class ClientBodyTempPath(DirectiveBase):
    def __init__(
        self,
        order : int,
        path : Path = Path("client_body_temp"),
        levels : Annotated[NonEmpty123Sequence, Is[_is_1_2_3]] | None = None,
    ):
        super().__init__(order, DIR_CLIENT_BODY_TEMP_PATH)
        self.add_arg(path)

        if levels is not None:
            for level in levels:
                self.add_arg(level)
