from ...Common import BuildArgsHelper, DirectiveBase, MimeType

class DefaultType(DirectiveBase):
    def __init__(
        self,
        mime : MimeType = MimeType.text__plain,
    ):
        args : list[str] = []

        BuildArgsHelper.add_enum_value(args, mime)

        super().__init__(
            "default_type",
            args,
        )

    @property
    def min_version(
        self,
    ) -> tuple[int, int, int]:
        return (0, 0, 0)
