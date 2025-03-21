from ....Common import Variable
from ....Common.Validators import NonEmptyString

class ArgsVariable(Variable):
    def __init__(
        self,
        arg_name: NonEmptyString,
    ):
        super().__init__(f"arg_{arg_name}")
