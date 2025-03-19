from ._DirectivesList import DIR_MERGE_SLASHES
from ...Common import DirectiveBase, OnOff

class MergeSlashes(DirectiveBase):
    def __init__(
        self,
        state : OnOff = OnOff.on,
    ):
        super().__init__(DIR_MERGE_SLASHES)
        self.add_arg(state)
