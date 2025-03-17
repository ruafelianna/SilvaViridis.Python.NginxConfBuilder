from ...Common import BuildArgsHelper, DirectiveBase, OnOff

class AbsoluteRedirect(DirectiveBase):
    def __init__(
        self,
        state : OnOff = OnOff.on,
    ):
        args : list[str] = []

        BuildArgsHelper.add_enum_value(args, state)

        super().__init__(
            "absolute_redirect",
            args,
        )

    @property
    def min_version(
        self,
    ) -> tuple[int, int, int]:
        return (1, 11, 8)
