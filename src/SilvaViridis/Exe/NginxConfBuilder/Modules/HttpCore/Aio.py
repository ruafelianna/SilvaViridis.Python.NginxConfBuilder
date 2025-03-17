from typing import Literal

from ...Common import BuildArgsHelper, DirectiveBase, OnOff

class Aio(DirectiveBase):
    def __init__(
        self,
        state : OnOff | Literal["threads"] = OnOff.off,
        pool : str | None = None,
    ):
        args : list[str] = []

        if isinstance(state, OnOff):
            BuildArgsHelper.add_enum_value(args, state)
        else:
            if not BuildArgsHelper.str_empty(pool):
                BuildArgsHelper.add_str_value(args, f"threads={pool}")
            else:
                BuildArgsHelper.add_str_value(args, "threads")

        super().__init__(
            "aio",
            args,
        )

    @property
    def min_version(
        self,
    ) -> tuple[int, int, int]:
        return (0, 8, 11)
