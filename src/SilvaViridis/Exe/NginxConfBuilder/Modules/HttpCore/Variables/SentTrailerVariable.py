from ....Common import Variable
from ....Common.Validators import NonEmptyString

class SentTrailerVariable(Variable):
    def __init__(
        self,
        field_name: NonEmptyString,
    ):
        super().__init__(f"sent_trailer_{field_name.lower().replace("-", "_")}")
