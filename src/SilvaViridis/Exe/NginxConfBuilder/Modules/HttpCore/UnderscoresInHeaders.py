from ._DirectivesList import DIR_UNDERSCORES_IN_HEADERS
from ...Common import DirectiveBase, OnOff

class UnderscoresInHeaders(DirectiveBase):
    def __init__(
        self,
        state : OnOff = OnOff.off,
    ):
        super().__init__(DIR_UNDERSCORES_IN_HEADERS)
        self.add_arg(state)
