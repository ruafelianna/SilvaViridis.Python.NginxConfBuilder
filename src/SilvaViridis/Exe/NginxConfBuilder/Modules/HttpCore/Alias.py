from ...Common import BuildArgsHelper, DirectiveBase, Path

class Alias(DirectiveBase):
    def __init__(
        self,
        path : Path,
    ):
        args : list[str] = []

        BuildArgsHelper.add_path(args, path)

        super().__init__(
            "alias",
            args,
        )

    @property
    def min_version(
        self,
    ) -> tuple[int, int, int]:
        return (0, 0, 0)
