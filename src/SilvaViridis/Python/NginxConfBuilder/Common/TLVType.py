from enum import Enum

class TLVType(Enum):
    alpn = 0x01,
    authority = 0x02
    unique_id = 0x05
    ssl = 0x20
    ssl_version = 0x21,
    ssl_cn = 0x22
    ssl_cipher = 0x23
    ssl_sig_alg = 0x24
    ssl_key_alg = 0x25
    ssl_verify = -1
    netns = 0x30
