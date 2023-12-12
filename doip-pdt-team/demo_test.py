import logging
import doiptypes
import binascii
import argparse

logging.basicConfig(level=logging.DEBUG)

logger = logging.getLogger("DoIP PDT team knowldege")

def U16ToByteArray(u16):
    u16=int(u16)
    logger.info("U16ToByteArray: u16=" + str(u16))
    res=bytearray([(u16 >> 8) & 0xFF, u16 & 0xFF])
    logger.info("U16ToByteArray: u16=" + str(u16) + " -> " + str(binascii.hexlify(res)))
    return res

class DemoTester:
    def __init__(self, host, port, testerAddr):
        logger.info("Tester:__init__")
        self.nodes = []
        self.active = 1
        self.port = port
        logger.info("  port:" + str(port))
        self.host = host
        logger.info("  host:" + host)
        self.testerAddr = testerAddr
        logger.info("  testerAddr:" + str(testerAddr))
      

# Parent class
class DemoTesterBase(DemoTester):
    def __init__ (self, args):
        logger.info("TesterBase:__init__")
        if (args.testerIP == None):
            raise Exception("missing arg testerIP")
        if (args.targetIP == None):
            raise Exception("missing arg targetIP")
        if (args.testerAddress == None):
            raise Exception("missing arg testerAddress")
        if (args.targetAddress == None):
            raise Exception("missing arg targetAddress")
        if (args.port == None):
            raise Exception("missing arg port");
  
        DemoTester.__init__(self, args.testerIP, args.port, args.testerAddress)
        self.testerIP=args.testerIP
        self.targetIP=args.targetIP
        self.route=args.route
        logger.info("TesterBase:targetIP=" + str(self.targetIP))
        self.targetAddress=args.targetAddress
        self.testerAddress=args.testerAddress
        self.testNode = DemoNode(self.targetIP, self.targetAddress, self)
        self.connected=False

class DemoNode:
    def __init__(self, address, identification, tester):
        logger.info("Node:__init__")
        self.active = 0
        self.identification = identification
        self.address = address
        self.tester = tester
        self.nodeType = -1
        self.maxTcpSockets = -1
        self.currTcpSockets = -1
        self.maxDataSize = -1
        self.powerMode = -1

    def __str__ (self):
        return f"{self.address[0]} >>> {self.identification} [{self.powerMode},\
             {self.nodeType},{self.maxTcpSockets},{self.currTcpSockets},{self.maxDataSize}]"
   
    def routingActivationReq (self, actNumber, oemdata):
        logger.info("Node:routingActivationReq")
        self.activationType = actNumber
        message = doiptypes.Message(doiptypes.RoutingActivationRequest(self.tester.testerAddr, actNumber, oemdata))
        try:
            logger.info("SEND[TCP]: " + str(self.address) + " >> " + binascii.hexlify(message.serialize()))
        except:
            logger.info("SEND[TCP]: " + str(self.address) + " >> " + str(binascii.hexlify(message.serialize())))
        print(message.serialize())

def main():
    parser = argparse.ArgumentParser(description='Mô tả về chương trình')
    parser.add_argument('--port', type=int, default=13400, help='Địa chỉ IP của Tester')
    parser.add_argument('--testerIP', type=str, default='10.200.220.10', help='Địa chỉ IP của Tester')
    parser.add_argument('--targetIP', type=str, default='10.200.220.1', help='Địa chỉ IP của Target')
    parser.add_argument('--testerAddress', type=int, default=1895, help="default: 1895 (0x767)")
    parser.add_argument('--targetAddress', type=int, default=1895, help="default: 1863 (0x747)")
    parser.add_argument('--route', type=int, default=0, help="default: 0 (0x00)")

    args = parser.parse_args()

    tester= DemoTesterBase(args)

    targetIP='10.200.220.1'
    targetAddress = '1863'
    node = DemoNode(targetIP, U16ToByteArray(targetAddress), tester)
    route = 2
    node.routingActivationReq(route, bytearray(4))

if __name__ == '__main__':
    main()
