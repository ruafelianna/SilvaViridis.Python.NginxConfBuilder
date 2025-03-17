from ...Common import BuildArgsHelper, DirectiveBase, OnOff

class ChunkedTransferEncoding(DirectiveBase):
    def __init__(
        self,
        state : OnOff = OnOff.on,
    ):
        args : list[str] = []

        BuildArgsHelper.add_enum_value(args, state)

        super().__init__(
            "chunked_transfer_encoding",
            args,
        )

    @property
    def min_version(
        self,
    ) -> tuple[int, int, int]:
        return (0, 0, 0)
