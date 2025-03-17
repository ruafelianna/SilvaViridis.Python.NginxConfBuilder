from typing import Literal, Sequence

from ...Common import BuildArgsHelper, DirectiveBase, Path

class ClientBodyTempPath(DirectiveBase):
    def __init__(
        self,
        path : Path = Path("client_body_temp"),
        levels : Sequence[Literal[1, 2, 3]] | None = None,
    ):
        args : list[str] = []

        BuildArgsHelper.add_path(args, path)

        if levels is not None:
            for level in levels:
                BuildArgsHelper.add_str_value(args, str(level))

        super().__init__(
            "client_body_temp_path",
            args,
        )

    @property
    def min_version(
        self,
    ) -> tuple[int, int, int]:
        return (0, 0, 0)
