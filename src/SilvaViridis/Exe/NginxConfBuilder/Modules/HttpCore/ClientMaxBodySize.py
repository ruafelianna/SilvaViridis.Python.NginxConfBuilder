from ...Common import (
    BuildArgsHelper,
    DirectiveBase,
    Size,
    SizeUnit,
)

class ClientMaxBodySize(DirectiveBase):
    def __init__(
        self,
        size : Size = Size(1, SizeUnit.megabytes),
    ):
        args : list[str] = []

        BuildArgsHelper.add_size(args, size)

        super().__init__(
            "client_max_body_size",
            args,
        )

    @property
    def min_version(
        self,
    ) -> tuple[int, int, int]:
        return (0, 0, 0)
