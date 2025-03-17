from typing import Literal

from ...Common import BuildArgsHelper, DirectiveBase, OnOff, Size

class Directio(DirectiveBase):
    def __init__(
        self,
        state : Size | Literal[OnOff.off] = OnOff.off,
    ):
        args : list[str] = []

        if isinstance(state, Size):
            BuildArgsHelper.add_size(args, state)
        else:
            BuildArgsHelper.add_enum_value(args, state)

        super().__init__(
            "directio",
            args,
        )

    @property
    def min_version(
        self,
    ) -> tuple[int, int, int]:
        return (0, 7, 7)
