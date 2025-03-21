from SilvaViridis.Exe.NginxConfBuilder.Common.Validators import NonEmptyString
from ....Common import Variable

class SentTrailerVariable(Variable):
    def __init__(
        self,
        field_name: NonEmptyString,
    ):
        super().__init__(f"sent_trailer_{field_name.lower().replace("-", "_")}")
