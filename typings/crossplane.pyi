from collections.abc import Sequence

from SilvaViridis.Python.NginxConfBuilder.Common import DirectiveDict

def build(
    payload : Sequence[DirectiveDict],
    indent: int = 4,
    tabs: bool = False,
    header: bool = False,
) -> str: ...
