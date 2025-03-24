from collections.abc import Mapping

from SilvaViridis.Python.Common.Types import NonEmptyString
from SilvaViridis.Python.Common.Web import MimeType

from ._DirectivesList import DIR_TYPES
from ...Common import DirectiveBase

class Types(DirectiveBase):
    def __init__(
        self,
        mapping : Mapping[MimeType, set[NonEmptyString]] = {
            MimeType.text__html: set(("html",)),
            MimeType.image__gif: set(("gif",)),
            MimeType.image__jpeg: set(("jpg",)),
        },
    ):
        super().__init__(DIR_TYPES)
        for mime, ext in mapping.items():
            self.add_directive(DirectiveBase(
                mime.value,
                list(ext),
            ))
