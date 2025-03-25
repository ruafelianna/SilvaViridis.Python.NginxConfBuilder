from SilvaViridis.Python.Common.Types import NonEmptyString

class Zone:
    def __init__(
        self,
        name : NonEmptyString,
    ):
        self._name = name

    def __str__(
        self,
    ) -> str:
        return f"${self.name}"

    @property
    def name(
        self,
    ) -> str:
        return self._name
