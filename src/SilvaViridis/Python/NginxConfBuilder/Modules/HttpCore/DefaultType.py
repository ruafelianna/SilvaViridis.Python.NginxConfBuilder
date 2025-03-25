from SilvaViridis.Python.Common.Web import MimeType

from ...Common import DirectiveBase

DIR_DEFAULT_TYPE = "default_type"

class DefaultType(DirectiveBase):
    def __init__(
        self,
        order : int,
        mime_type : MimeType = MimeType.text__plain,
    ):
        super().__init__(order, DIR_DEFAULT_TYPE)
        self.add_arg(mime_type)
