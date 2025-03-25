from ...Common import DirectiveBase, OnOff

DIR_MERGE_SLASHES = "merge_slashes"

class MergeSlashes(DirectiveBase):
    def __init__(
        self,
        order : int,
        state : OnOff = OnOff.on,
    ):
        super().__init__(order, DIR_MERGE_SLASHES)
        self.add_arg(state)
