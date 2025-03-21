from enum import Enum

class JSWType(Enum):
    signed = "JWS"
    encrypted = "JWE"
    nested = "JWT"
