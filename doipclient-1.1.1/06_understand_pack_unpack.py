import struct
import logging
import binascii

logger = logging.getLogger("test")
logging.basicConfig(level=logging.DEBUG)

def wrapper_data(source_address, target_address, user_data):
    return (
        struct.pack("!HH", source_address, target_address)
        + user_data
    )

def unwrapper_data():
    pass

def main():
    source_address = 1895
    target_address = 1863
    user_data_hex = "1001"
    user_data_bytes = bytes.fromhex(user_data_hex)
    payload_type = 0x8001

    payload_data = wrapper_data(source_address, target_address, user_data_bytes)
    print(payload_data)
    print("Tester:receiveMsg:got:" + str(binascii.hexlify(payload_data)))
    logger.debug(
        "Sending DoIP Message: Type: 0x{:X}, Payload Size: {}, Payload: {}".format(
            payload_type,
            len(payload_data),
            " ".join(f"{byte:02X}" for byte in payload_data),
        )
    )

if __name__ == '__main__':
    main()
