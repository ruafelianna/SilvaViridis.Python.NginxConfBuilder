from SilvaViridis.Python.Common.Types import NonEmptySequence, NonEmptyString

from ...Common import DirectiveBase, Variable

DIR_AUTH_JWT_CLAIM_SET = "auth_jwt_claim_set"

class AuthJwtClaimSet(DirectiveBase):
    def __init__(
        self,
        order : int,
        variable : Variable,
        keys : NonEmptySequence[NonEmptyString],
    ):
        super().__init__(order, DIR_AUTH_JWT_CLAIM_SET)
        self.add_arg(variable)

        for key in keys:
            self.add_arg(key)

    @property
    def min_version(
        self,
    ) -> tuple[int, int, int]:
        return (1, 11, 10)
