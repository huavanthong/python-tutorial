"""
    File_name       :   DoIPLibrary.py
    Class name      :   DoIPLibrary
    Description     :   This File contains the class to communicate with the DoIP server in the target
    Date        Version   Author             Comments
    **************************************************************************************
    12/16/2020  1.0       ala2cob            Initial Development
	20/1/2021	1.1		  myo1cob            Adapatation in Routing request activation call
    **************************************************************************************
"""
import socket
import time
from threading import Lock, Thread, Event
import schedule
import binascii
from robot.api import logger
from robot.libraries.BuiltIn import BuiltIn

# Constants
# DoIP Header Structure : <protocol version><inverse protocol version><payload type><payload length><payload>
# Payload format : <local ecu address> <optional: target ecu address> <optional message ><ASRBISO><ASRBOEM>

PROTOCOL_VERSION = DOIP_PV = '02'
INVERSE_PROTOCOL_VERSION = DOIP_IPV = 'FD'

# Payload type definitions#
DOIP_GENERIC_NEGATIVE_ACKNOWLEDGE = DOIP_NARP = '0000'
DOIP_VEHICLE_ID_REQUEST = '0001'
DOIP_VEHICLE_ID_REQUEST_W_EID = '0002'
DOIP_VEHICLE_ID_REQUEST_W_VIN = '0003'
DOIP_VEHICLE_ANNOUNCEMENT_ID_RESPONSE = '0004'
# DOIP_ROUTING_ACTIVATION_REQUEST : <0005><source address><activation type><00000000>
DOIP_ROUTING_ACTIVATION_REQUEST = DOIP_RAR = '0005'
DOIP_ROUTING_ACTIVATION_RESPONSE = '0006'
DOIP_ALIVE_CHECK_REQUEST = '0007'
DOIP_ALIVE_CHECK_RESPONSE = '0008'
# 0x009-0x4000: Reserved by ISO13400
DOIP_ENTITY_STATUS_REQUEST = '4001'
DOIP_ENTITY_STATUS_RESPONSE = '4002'
DOIP_DIAGNOSTIC_POWER_MODE_INFO_REQUEST = '4003'
DOIP_DIAGNOSTIC_POWER_MODE_INFO_RESPONSE = '4004'
# 0x4005-0x8000 Reserved by ISO13400
DOIP_DIAGNOSTIC_MESSAGE = DOIP_UDS = '8001'
DOIP_DIAGNOSTIC_POSITIVE_ACKNOWLEDGE = '8002'
DOIP_DIAGNOSTIC_NEGATIVE_ACKNOWLEDGE = '8003'
DOIP_EMPTY = ''
ACTIVATION_SPACE_RESERVED_BY_ISO = ASRBISO = '00000000'

payloadTypeDescription = {
    DOIP_GENERIC_NEGATIVE_ACKNOWLEDGE: "Generic negative response",
    DOIP_VEHICLE_ID_REQUEST: "Vehicle ID request",
    DOIP_VEHICLE_ID_REQUEST_W_EID: "Vehicle ID request with EID",
    DOIP_VEHICLE_ID_REQUEST_W_VIN: "Vehicle ID request with VIN",
    DOIP_VEHICLE_ANNOUNCEMENT_ID_RESPONSE: "Vehicle announcement ID response",
    DOIP_ROUTING_ACTIVATION_REQUEST: "Routing activation request",
    DOIP_ROUTING_ACTIVATION_RESPONSE: "Routing activation response",
    DOIP_ALIVE_CHECK_REQUEST: "Alive check request",
    DOIP_ALIVE_CHECK_RESPONSE: "Alive check response",
    DOIP_ENTITY_STATUS_REQUEST: "Entity status request",
    DOIP_ENTITY_STATUS_RESPONSE: "Entity status response",
    DOIP_DIAGNOSTIC_POWER_MODE_INFO_REQUEST: "Diagnostic power mode info request",
    DOIP_DIAGNOSTIC_POWER_MODE_INFO_RESPONSE: "Power mode info response",
    DOIP_DIAGNOSTIC_MESSAGE: "Diagnostic message",
    DOIP_DIAGNOSTIC_POSITIVE_ACKNOWLEDGE: "Diagnostic positive acknowledge",
    DOIP_DIAGNOSTIC_NEGATIVE_ACKNOWLEDGE: "Diagnostic negative acknowledge",
    DOIP_EMPTY: "Empty payload"
}

# Global vars
messages = {}


class DoIPLibrary:
    """
    DoIP Library Provides interface to establish DoIP communication with the DoIP server in ECU.
    It enables a socket communication to communicate with DoIP gateway in the ECU.
    
    1. Diagnostics UDS commands can be sent.
    
    2. Tester Present can be enabled with user-defined interval.
    
    3. Routing Activation request will be sent automatically from the DoIP Library for every UDS request.
    """
    ROBOT_LIBRARY_DOC_FORMAT = 'reST'
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
    ROBOT_LIBRARY_VERSION = 1.0

    def __init__(self):
        self.target_ip = ""
        self.target_addr = ""
        self.tester_ip = ""
        self.targetPort = 13400
        self.port = 0
        self.tester_addr = ""
        self.tcp_socket = None
        self.isConnected = False
        self.activation_type = ""
        self.tester_not_present = False
        self.thread_interval = 0
        self.tester_thread = Thread()
        self.lock = Lock()
        self.kill_threads = False

    def doip_init(self):
        """
        This function is used to initiate DoIp connection between target and the tester systems.
        
        :return: None. 
        """
        # Read from TestBench.py
        # self.tester_ip = BuiltIn().get_variable_value("${DOIP_TESTER_IP}")
        # self.target_ip = BuiltIn().get_variable_value("${DOIP_TARGET_IP}")
        # self.target_addr = BuiltIn().get_variable_value("${DOIP_TARGET_LOGICAL_ADDR}")
        # self.tester_addr = BuiltIn().get_variable_value("${DOIP_TESTER_LOGICAL_ADDR}")
        # self.activation_type = BuiltIn().get_variable_value("${DOIP_ROUTING_ACTIVATION_TYPE}")

        self.tester_ip = "192.168.108.1"
        self.target_ip = "192.168.108.1"
        self.target_addr = "3300"
        # self.tester_addr = "3584"
        self.activation_type = "02"

        # self.tester_ip = BuiltIn().get_variable_value('${SimulationTarget.DOIP_TARGET_IP}')
        # self.target_ip = BuiltIn().get_variable_value('${SimulationTarget.DOIP_TARGET_IP}')
        # self.target_addr = BuiltIn().get_variable_value('${SimulationTarget.DOIP_TARGET_LOGICAL_ADDR}')
        # self.tester_addr = BuiltIn().get_variable_value('${SimulationTarget.DOIP_TESTER_LOGICAL_ADDR}')
        # self.activation_type = BuiltIn().get_variable_value('${SimulationTarget.DOIP_ROUTING_ACTIVATION_TYPE}')

        try:
            self.tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # self._TCP_Socket.setsockopt(socket.IPPROTO_TCP, 12, 1)#supposedly, 12 is TCP_QUICKACK option id
            self.tcp_socket.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)  # immediately send to wire without delay
            self.tcp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,
                                       1)  # allows different sockets to reuse ipaddress
            self.tcp_socket.settimeout(15)
            self.tcp_socket.bind((self.tester_ip, self.port))
            logger.info("Socket successfully created: Bound to %s:%d" % (
                self.tcp_socket.getsockname()[0], self.tcp_socket.getsockname()[1]))
            self.tester_ip = self.tcp_socket.getsockname()[0]
            self.port = self.tcp_socket.getsockname()[1]
            if self._connect_to_server() == 0:
                pass
            else:
                BuiltIn().fail("DoIP Initialization Unsuccessful: Connect to DoIP server failed")

        except socket.error as err:
            logger.error("Socket creation Failed with error: %s" % err)
            self.tcp_socket = None
            BuiltIn().fail("DoIP Initialization Failed")

    def doip_teardown(self):
        """
        Stop all running threads and close the socket with the DoIP server.
        
        :return: None.
        """
        self.kill_threads = True
        if self.tester_thread.is_alive():
            self.tester_not_present = True
            self.tester_thread.join()
        self.tcp_socket.close()
        self.isConnected = False

    def _connect_to_server(self):
        """
        This method establish connection with the DoIP server.
        """
        if self.isConnected:
            logger.warn("Error :: Already connected to a server. Close the connection before starting a new one\n")
        else:
            if self.tcp_socket is not None:
                try:
                    logger.info("Connecting to DoIP Server at %s:%d... " % (self.target_ip, self.targetPort))
                    self.tcp_socket.connect((self.target_ip, self.targetPort))
                    self.isConnected = True
                    logger.info("Connection to DoIP established\n")
                    return 0
                except socket.error as err:
                    logger.error("Unable to connect to socket at %s:%d. Socket failed with error: %s" % (
                        self.target_ip, self.targetPort, err))
                    self.isConnected = False
            else:
                return -1

    def _routing_activation_request(self, keep_alive=0):
        """
        This method send routing activation request to the server. This is send before every diagnostic message.
        """

        if self.isConnected:
            doip_header = PROTOCOL_VERSION + INVERSE_PROTOCOL_VERSION + DOIP_ROUTING_ACTIVATION_REQUEST
            payload = self.tester_addr + self.activation_type + ASRBISO
            payload_length = "%.8X" % (len(payload) // 2)
            activation_string = doip_header + payload_length + payload

            if keep_alive == 0:
                logger.info("DoIP SEND ::")
                _format_msg(activation_string)
                logger.info("Requesting routing activation...")
            try:
                for i in range(5):
                    self.tcp_socket.send(bytes.fromhex(activation_string))
                    time.sleep(1)
                    activation_response = self.tcp_socket.recv(1024)
                    print("activation response",activation_response)
                    if activation_response!=b'':
                       break

                if keep_alive == 1:
                    return activation_response

                logger.info("DoIP RECV ::")
                response = _format_msg(activation_response)
                print(response)
                if DOIP_ROUTING_ACTIVATION_RESPONSE in response.keys():
                  if response[DOIP_ROUTING_ACTIVATION_RESPONSE][0]["payload"][0:2] == '10':
                      logger.info("Routing activated with ECU: " +
                                response[DOIP_ROUTING_ACTIVATION_RESPONSE][0]["target_addr"])
                      return 0
                  else:
                      logger.error("Unable to activate routing")
                      return -1
                else:
                      return -1
            except socket.error as err:
                self.kill_threads = True
                if keep_alive == 0:
                    logger.error("Unable to activate routing with ECU: " + self.target_ip +
                             ". Socket failed with error: " + str(err))
                return -1
        else:
            logger.error("Unable to request routing activation. Currently not connected to a DoIP server")
            return -1

    def send_diag_message(self, message):
        """
        This method send the diagnostic message to the target using DoIP protocol.

        :param:
            :message: Diagnostic message.
        
        :return:
            :payload: array of payload data extracted from the DoIP responses.
            :Diag_response: Array of response of type Diagnostic message.
        """
        self.lock.acquire()
        
        if self.isConnected:
            try:
                doip_header = PROTOCOL_VERSION + INVERSE_PROTOCOL_VERSION + DOIP_DIAGNOSTIC_MESSAGE
                payload = self.tester_addr + self.target_addr + message
                payload_length = "%.8X" % (len(payload) // 2)
                diag_message = doip_header + payload_length + payload
                logger.info(self._routing_activation_request())
                logger.info("DoIP SEND Diag::")
                _format_msg(diag_message)
                self.tcp_socket.send(bytes.fromhex(diag_message))
                time.sleep(1)
                diag_resp = self.tcp_socket.recv(1024)
                logger.info("DoIP RECV ::")
                response = _format_msg(diag_resp)
                if DOIP_DIAGNOSTIC_POSITIVE_ACKNOWLEDGE in response.keys():
                    if DOIP_DIAGNOSTIC_MESSAGE in response.keys():
                        payload = []
                        diag_data = []
                        for i in response[DOIP_DIAGNOSTIC_MESSAGE]:
                            payload.append(i["payload"])
                            diag_data.append(i["payload"][0:4])
                        self.lock.release()
                        return payload, response[DOIP_DIAGNOSTIC_MESSAGE]
                    else:
                        self.lock.release()
                        logger.error("Received positive acknowledgement. Failed to receive response message")
                        self.kill_threads = True
                        BuiltIn().fail("DOIP: Send Diag Failed")
                elif DOIP_DIAGNOSTIC_NEGATIVE_ACKNOWLEDGE in response.keys():
                    self.lock.release()
                    logger.error("Received negative acknowledgement.")
                    self.kill_threads = True
                    BuiltIn().fail("DOIP: Send Diag Failed")
                else:
                    self.lock.release()
                    self.kill_threads = True
                    BuiltIn().fail("DOIP: Send Diag Failed")

            except socket.error as err:
                self.lock.release()
                logger.error("Unable to send message to ECU: " + self.target_ip + ". Socket failed with error: " + str(
                    err))
                self.kill_threads = True
                BuiltIn().fail("DOIP: Send Diag Failed")
        else:
            self.lock.release()
            logger.error("Not currently connected to a server")
            self.kill_threads = True
            BuiltIn().fail("DOIP: Send Diag Failed")

    def begin_tester_present(self, interval):
        """
        Method to send tester present periodically to the server.
        
        :param:
            :interval: Time interval in Seconds.
        
        :return: None.
        """
        message = '3E80'
        doip_header = PROTOCOL_VERSION + INVERSE_PROTOCOL_VERSION + DOIP_DIAGNOSTIC_MESSAGE
        payload = self.tester_addr + self.target_addr + message
        payload_length = "%.8X" % (len(payload) // 2)
        diag_message = doip_header + payload_length + payload

        self.thread_interval = int(interval)
        logger.info("DoIP SEND Diag::")
        _format_msg(diag_message)
        self.tester_not_present = False
        self.tester_thread = Thread(target=self._tester_present, args=(self.thread_interval, diag_message,))
        self.tester_thread.start()

    def end_tester_present(self):
        """
        Stop sending tester present signal.
        
        :return: None.
        """
        self.tester_not_present = True
        if self.tester_thread.is_alive():
            self.tester_thread.join(timeout=self.thread_interval + 5)
        if self.tester_thread.is_alive():
            self.kill_threads = True
            logger.info("DoIP: End Tester Present Fail")
        else:
            logger.info("End Tester Present Successful")

    def _tester_present(self, interval, data):

        def _scheduled_task():
            self.lock.acquire()
            if self.isConnected:
                try:
                    self._routing_activation_request(keep_alive=1)
                    self.tcp_socket.send(bytes.fromhex(data))
                    
                    time.sleep(1)
                    diag_resp = self.tcp_socket.recv(1024)
                except Exception as err:
                    self.kill_threads = True
            self.lock.release()
        schedule.every(interval).seconds.do(_scheduled_task)
        while not self.tester_not_present:
            schedule.run_pending()
            time.sleep(2)


def _format_msg(data):
    """
    This method extracts and display the formatted message.
    """
    global messages
    messages = {}
    message = {}
    if type(data).__name__ == 'bytes':
        data = binascii.hexlify(data)
        data = data.decode("utf-8")
    message["version"] = data[0:2]
    message["inverse_version"] = data[2:4]
    message["payload_type"] = data[4:8]
    message["payload_length"] = data[8:16]
    message["src_addr"] = data[16:20]
    if message["payload_type"] == DOIP_RAR:
        message["target_addr"] = None
        payload_start = 20
    else:
        message["target_addr"] = data[20:24]
        payload_start = 24
    if message["payload_length"] != '':
        payload_length = int(message["payload_length"], 16)
    else:
        payload_length = 0
    message["payload"] = data[payload_start:16 + payload_length * 2]
    
    logger.info(data)
    
    logger.info("Protocol Version         : " + message["version"])
    logger.info("Inv. Protocol Version    : " + message["inverse_version"])
    logger.info("Payload Type             : " + message["payload_type"])
    
    logger.info("Payload Type Description : " + payloadTypeDescription[message["payload_type"]])
    logger.info("Payload Length           : " + message["payload_length"])
    logger.info("Source Address           : " + message["src_addr"])
    logger.info("Target Address           : " + str(message["target_addr"]))
    logger.info("Payload                  : " + message["payload"])
    logger.info(" ")

    msg_end = 16 + payload_length * 2
    if msg_end < len(data):
        _format_msg(data[msg_end:])
    if message["payload_type"] in messages.keys():
        messages[message["payload_type"]].append(message)
    else:
        messages[message["payload_type"]] = [message]
    return messages
