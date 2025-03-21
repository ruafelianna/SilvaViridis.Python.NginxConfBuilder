from ....Common import Variable
from ....Common.Validators import NonEmptyString

class SentHttpVariable(Variable):
    def __init__(
        self,
        field_name: NonEmptyString,
    ):
        super().__init__(f"sent_http_{field_name.lower().replace("-", "_")}")
