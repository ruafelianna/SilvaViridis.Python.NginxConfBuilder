from SilvaViridis.Python.Common.Text import NonEmptyString

from ....Common import Variable

class HttpVariable(Variable):
    def __init__(
        self,
        field_name: NonEmptyString,
    ):
        super().__init__(f"http_{field_name.lower().replace("-", "_")}")
