from SilvaViridis.Python.Common.Text import NonEmptyString

from ....Common import Variable

class CookieVariable(Variable):
    def __init__(
        self,
        cookie_name: NonEmptyString,
    ):
        super().__init__(f"cookie_{cookie_name}")
