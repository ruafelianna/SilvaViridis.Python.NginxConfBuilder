from SilvaViridis.Python.Common.Web import MimeType

from ...Common import DirectiveBase

DIR_DEFAULT_TYPE = "default_type"

class DefaultType(DirectiveBase):
    def __init__(
        self,
        mime_type : MimeType = MimeType.text__plain,
    ):
        super().__init__(DIR_DEFAULT_TYPE)
        self.add_arg(mime_type)
