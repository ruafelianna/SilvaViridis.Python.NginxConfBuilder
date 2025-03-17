from .BuildArgsHelper import BuildArgsHelper

class Path:
    def __init__(
        self,
        value : str,
    ):
        if BuildArgsHelper.str_empty(value):
            ValueError("`path` cannot be empty")

        self.value = value
