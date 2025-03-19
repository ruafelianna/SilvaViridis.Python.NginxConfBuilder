from SilvaViridis.Python.Common.Web import MimeType

from ._DirectivesList import DIR_DEFAULT_TYPE
from ...Common import DirectiveBase

class DefaultType(DirectiveBase):
    def __init__(
        self,
        mime_type : MimeType = MimeType.text__plain,
    ):
        super().__init__(DIR_DEFAULT_TYPE)
        self.add_arg(mime_type)
