from typing import Literal

from ...Common import BuildArgsHelper, DirectiveBase, OnOff

class ClientBodyInFileOnly(DirectiveBase):
    def __init__(
        self,
        state : OnOff | Literal["clean"] = OnOff.off,
    ):
        args : list[str] = []

        if isinstance(state, OnOff):
            BuildArgsHelper.add_enum_value(args, state)
        else:
            BuildArgsHelper.add_str_value(args, "clean")

        super().__init__(
            "client_body_in_file_only",
            args,
        )

    @property
    def min_version(
        self,
    ) -> tuple[int, int, int]:
        return (0, 0, 0)
