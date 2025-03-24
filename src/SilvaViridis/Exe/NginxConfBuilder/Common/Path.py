from SilvaViridis.Python.Common.Types import NonEmptyString

class Path:
    def __init__(
        self,
        value : NonEmptyString,
    ):
        self._value = value

    def __str__(
        self,
    ):
        return self.value

    @property
    def value(
        self,
    ) -> str:
        return self._value
