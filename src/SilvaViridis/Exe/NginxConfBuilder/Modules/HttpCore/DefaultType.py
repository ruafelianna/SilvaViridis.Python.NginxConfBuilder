from .DirectivesList import DIR_DEFAULT_TYPE
from ...Common import DirectiveBase, MimeType

class DefaultType(DirectiveBase):
    def __init__(
        self,
        mime_type : MimeType = MimeType.text__plain,
    ):
        super().__init__(DIR_DEFAULT_TYPE)
        self.add_enum_arg(mime_type)

    @property
    def min_version(
        self,
    ) -> tuple[int, int, int]:
        return (0, 0, 0)
