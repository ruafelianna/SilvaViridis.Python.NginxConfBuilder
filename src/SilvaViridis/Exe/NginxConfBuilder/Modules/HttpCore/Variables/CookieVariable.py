from ....Common import Variable
from ....Common.Validators import NonEmptyString

class CookieVariable(Variable):
    def __init__(
        self,
        cookie_name: NonEmptyString,
    ):
        super().__init__(f"cookie_{cookie_name}")
