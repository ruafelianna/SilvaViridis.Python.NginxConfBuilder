from typing import Annotated, Sequence

from ._DirectivesList import DIR_AUTH_JWT_CLAIM_SET
from ...Common import DirectiveBase, Variable
from ...Common.Validators import NonEmptySequenceValidator, NonEmptyString

KeyList = Annotated[Sequence[NonEmptyString], NonEmptySequenceValidator]

class AuthJwtClaimSet(DirectiveBase):
    def __init__(
        self,
        variable : Variable,
        keys : KeyList,
    ):
        super().__init__(DIR_AUTH_JWT_CLAIM_SET)
        self.add_arg(variable)

        for key in keys:
            self.add_arg(key)

    @property
    def min_version(
        self,
    ) -> tuple[int, int, int]:
        return (1, 11, 10)
