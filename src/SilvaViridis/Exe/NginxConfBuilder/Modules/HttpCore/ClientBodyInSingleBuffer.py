from ...Common import BuildArgsHelper, DirectiveBase, OnOff

class ClientBodyInSingleBuffer(DirectiveBase):
    def __init__(
        self,
        state : OnOff = OnOff.off,
    ):
        args : list[str] = []

        BuildArgsHelper.add_enum_value(args, state)

        super().__init__(
            "client_body_in_single_buffer",
            args,
        )

    @property
    def min_version(
        self,
    ) -> tuple[int, int, int]:
        return (0, 0, 0)
