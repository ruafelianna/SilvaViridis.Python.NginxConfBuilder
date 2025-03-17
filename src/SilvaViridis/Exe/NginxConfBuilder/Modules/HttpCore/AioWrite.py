from ...Common import BuildArgsHelper, DirectiveBase, OnOff

class AioWrite(DirectiveBase):
    def __init__(
        self,
        state : OnOff = OnOff.off,
    ):
        args : list[str] = []

        BuildArgsHelper.add_enum_value(args, state)

        super().__init__(
            "aio_write",
            args,
        )

    @property
    def min_version(
        self,
    ) -> tuple[int, int, int]:
        return (1, 9, 13)
