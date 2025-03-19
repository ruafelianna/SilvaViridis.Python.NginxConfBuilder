from ._DirectivesList import DIR_INTERNAL
from ...Common import DirectiveBase

class Internal(DirectiveBase):
    def __init__(
        self,
    ):
        super().__init__(DIR_INTERNAL)

    @property
    def min_version(
        self,
    ) -> tuple[int, int, int]:
        return (0, 0, 0)
