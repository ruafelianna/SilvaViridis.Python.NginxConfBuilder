from collections.abc import Mapping

from SilvaViridis.Python.Common.Types import NonEmptyString
from SilvaViridis.Python.Common.Web import MimeType

from ...Common import DirectiveBase

DIR_TYPES = "types"

class Types(DirectiveBase):
    def __init__(
        self,
        order : int,
        mapping : Mapping[MimeType, set[NonEmptyString]] = {
            MimeType.text__html: set(("html",)),
            MimeType.image__gif: set(("gif",)),
            MimeType.image__jpeg: set(("jpg",)),
        },
    ):
        super().__init__(order, DIR_TYPES)
        for i, (mime, ext) in enumerate(mapping.items()):
            self.add_directive(DirectiveBase(
                i,
                mime.value,
                list(ext),
            ))
