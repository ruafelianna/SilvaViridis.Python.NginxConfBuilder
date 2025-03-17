from ...Common import (
    BuildArgsHelper,
    DirectiveBase,
    Size,
)

class ConnectionPoolSize(DirectiveBase):
    def __init__(
        self,
        size : Size = Size(512),
    ):
        args : list[str] = []

        BuildArgsHelper.add_size(args, size)

        super().__init__(
            "connection_pool_size",
            args,
        )

    @property
    def min_version(
        self,
    ) -> tuple[int, int, int]:
        return (0, 0, 0)
