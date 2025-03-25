from ....Common import TLVType, Variable

class ProxyProtocolTlvVariable(Variable):
    def __init__(
        self,
        tlv_type: TLVType,
    ):
        super().__init__(f"proxy_protocol_tlv_{tlv_type.name}")
