from doipclient.messages import *


hex_payload = "54 45 53 54 56 49 4E 30 30 30 30 30 31 32 33 34 35 30 00 12 34 56 78 9A BC 12 34 56 78 9A BC 00"

# Chia chuỗi hex thành từng cặp ký tự
hex_values = hex_payload.split()

# Chuyển từng cặp ký tự hex thành giá trị ASCII
ascii_values = [bytes.fromhex(hex_value).decode('utf-8') for hex_value in hex_values]

# Kết hợp giá trị ASCII thành một chuỗi
resulting_string = "".join(ascii_values)

print(resulting_string)

payload_type_to_message = {
    0x0000: GenericDoIPNegativeAcknowledge,
    0x0001: VehicleIdentificationRequest,
    0x0002: VehicleIdentificationRequestWithEID,
    0x0003: VehicleIdentificationRequestWithVIN,
    0x0004: VehicleIdentificationResponse,
    0x0005: RoutingActivationRequest,
    0x0006: RoutingActivationResponse,
    0x0007: AliveCheckRequest,
    0x0008: AliveCheckResponse,
    0x4001: DoipEntityStatusRequest,
    0x4002: EntityStatusResponse,
    0x4003: DiagnosticPowerModeRequest,
    0x4004: DiagnosticPowerModeResponse,
    0x8001: DiagnosticMessage,
    0x8002: DiagnosticMessagePositiveAcknowledgement,
    0x8003: DiagnosticMessageNegativeAcknowledgement,
}


payload_type_to_message[self.payload_type].unpack(
                        self.payload, self.payload_size