from collections.abc import Sequence

from SilvaViridis.Python.Common.Collections import NonEmptySequence
from SilvaViridis.Python.Common.Web import HttpMethod

from ..HttpAccess import Allow, Deny
from ..HttpAuthBasic import AuthBasic, AuthBasicUserFile
from ..HttpAuthJwt import AuthJwt, AuthJwtKeyFile, AuthJwtKeyRequest, AuthJwtType, AuthJwtRequire
from ..HttpLog import AccessLog
from ...Common import DirectiveBase

DIR_LIMIT_EXCEPT = "limit_except"

type AccessDirective = Allow | Deny | AuthBasic | AuthBasicUserFile | AuthJwt | AuthJwtKeyFile | AuthJwtKeyRequest | AuthJwtType | AuthJwtRequire

class LimitExcept(DirectiveBase):
    def __init__(
        self,
        order : int,
        methods : NonEmptySequence[HttpMethod],
        access_list : Sequence[AccessDirective] = [],
        access_log : AccessLog | None = None,
    ):
        super().__init__(order, DIR_LIMIT_EXCEPT)

        for method in methods:
            self.add_arg(method.name)

        for directive in access_list:
            self.add_directive(directive)

        self.add_directive(access_log)
