from SilvaViridis.Python.Common.Text import StringHelper as SH

class Path:
    def __init__(
        self,
        value : str,
    ):
        if SH.is_none_or_whitespace(value):
            ValueError("`path` cannot be empty")

        self.value = value
