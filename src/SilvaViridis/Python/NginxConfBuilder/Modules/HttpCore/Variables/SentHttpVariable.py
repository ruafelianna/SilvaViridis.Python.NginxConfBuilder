from SilvaViridis.Python.Common.Types import NonEmptyString

from ....Common import Variable

class SentHttpVariable(Variable):
    def __init__(
        self,
        field_name: NonEmptyString,
    ):
        super().__init__(f"sent_http_{field_name.lower().replace("-", "_")}")
