import logging
import binascii

logging.basicConfig(level=logging.DEBUG)

logger = logging.getLogger("Bytes tutorial")

def U16ToByteArray(u16):
    u16=int(u16)
    logger.info("U16ToByteArray: u16=" + str(u16))
    res=bytearray([(u16 >> 8) & 0xFF, u16 & 0xFF])
    logger.info("U16ToByteArray: u16=" + str(u16) + " -> " + str(binascii.hexlify(res)))
    return res

def test_U16ToByteArray():
    targetAddress = 1863
    result = U16ToByteArray(targetAddress)
    print("What is value: ", result)
    hex_string = binascii.hexlify(result)
    print("Convert byte array into value hexa: ", hex_string)

    print("Decode hexa format to : ", hex_string.decode('utf-8'))

def check_DoIP_Header(prot=0x02, protInv=0xFD, payloadType=0x8001, payloadLen=None, payload=bytearray(), doPrint=False):
    if payloadLen==None:
        payloadLen=len(payload)
    hdr=bytearray(8)
    hdr[0]=prot;
    hdr[1]=protInv;
    hdr[2]=((payloadType >> 8) & 0xFF);
    print("Check element 2: ", hdr[2])
    hdr[3]=((payloadType >> 0) & 0xFF);
    print("Check element 3: ", hdr[3])
    hdr[4]=((payloadLen >> 24) & 0xFF);
    print("Check element 4: ", hdr[4])
    hdr[5]=((payloadLen >> 16) & 0xFF);
    hdr[6]=((payloadLen >>  8) & 0xFF);
    hdr[7]=((payloadLen >>  0) & 0xFF);
    payload=payload
    doPrint = True
    if (doPrint):
        logger.info("DoipMsg len=" + str(len(payload)))
        logger.info("   hdr:" + str(binascii.hexlify(hdr)))
        logger.info("   payload:" + str(binascii.hexlify(payload)))
    
    data=hdr + payload
    message=None
    print("Getting data: ", data)
    print("Message is: ", message)

def test_check_DoIP_Header():
    check_DoIP_Header()

def main_function_a():
    # test_U16ToByteArray()
    test_check_DoIP_Header()

if __name__ == '__main__':
    main_function_a()
