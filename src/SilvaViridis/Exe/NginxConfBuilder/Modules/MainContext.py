from .HttpCore import Http
from ..Common import DirectiveBase

class MainContext(DirectiveBase):
    def __init__(
        self,
        http : Http | None = None,
    ):
        super().__init__("main")
        self.add_directive(http)
