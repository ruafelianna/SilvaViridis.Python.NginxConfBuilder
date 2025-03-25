from SilvaViridis.Python.Common.Types import NonEmptyString

from ....Common import Variable

class ArgsVariable(Variable):
    def __init__(
        self,
        arg_name: NonEmptyString,
    ):
        super().__init__(f"arg_{arg_name}")
