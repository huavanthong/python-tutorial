# This file contains the global configuration to be used in the Library
GLOBAL_TESTRUN_TIMEOUT = 30

# DoIP
DOIP_TARGET_IP = "172.17.0.1"  # IP address of CSB Board, can use VLAN 120
DOIP_TESTER_IP = "172.17.0.20"
DOIP_TARGET_LOGICAL_ADDR = "0747"
DOIP_TESTER_LOGICAL_ADDR = "0767"
DOIP_ROUTING_ACTIVATION_TYPE = "02"

# SOMEiP
SOMEIP_TESTER_IP = "10.210.220.5"
SOMEIP_TARGET_IP = "10.210.220.4"
SOMEIP_TESTER_PORT = 42987
SOMEIP_BROADCAST_PORT = 30490
SOMEIP_BROADCAST_IP = "239.210.224.245"
SOMEIP_DEVICE_NAME = "eth1.210"

# SOMEiPDiag

SOMEIPDIAG_TESTER_PORT = 42988


# SSH Configuration

#CSB
SSH1_IP = "10.210.220.4"
SSH1_USERNAME = "root"
SSH1_PASSWORD = ""  # password should be updated
SSH1_TIMEOUT = 10

#MMB
SSH2_IP = "10.210.220.1"
SSH2_USERNAME = "root"
SSH2_PASSWORD = ""  # password should be updated
SSH2_TIMEOUT = 10

# SSH1 Configuration for CSB TCP DUMP
Log_SSH1_IP = '10.210.220.4'
Log_SSH1_USERNAME = 'root'
Log_SSH1_PASSWORD = ''  # password should be updated
Log_SSH1_TIMEOUT = 10

# SSH2 Configuration for CSB DLT Trace
Log_SSH2_IP = '10.210.220.4'
Log_SSH2_USERNAME = 'root'
Log_SSH2_PASSWORD = ''  # password should be updated
Log_SSH2_TIMEOUT = 10

# SSH3 Configuration for MMB TCP DUMP
Log_SSH3_IP = '10.210.220.1'
Log_SSH3_USERNAME = 'root'
Log_SSH3_PASSWORD = ''  # password should be updated
Log_SSH3_TIMEOUT = 10

# SSH4 Configuration for MMB DLT Trace
Log_SSH4_IP = '10.210.220.1'
Log_SSH4_USERNAME = 'root'
Log_SSH4_PASSWORD = ''  # password should be updated
Log_SSH4_TIMEOUT = 10

# Tuner
TUNER_STATION_PORT = 42989
TUNER_STATIONLIST_PORT = 42990

# PPS
COM_PORT_PPS = "/dev/ttyUSB0"
BAUD_RATE_PPS = 9600

# SignalGen1
HOST_SIG1 = "10.169.193.126"
PORT_SIG1 = "5025"

# SignalGen2
HOST_SIG2 = "10.169.192.88"
PORT_SIG2 = "5025"

# Software_update_SOME/IP service
SERVER_IP = "10.210.220.5"
SERVER_PORT = 8000
SOMEIP_SW_UPDATE_TESTER_PORT = 30509
SW_UPDATE_BASE_URL = "http://10.210.220.5:8000/fileServer/"
SW_UPDATE_PASSWORD = "dummy"

# AVB
AVB_INTERFACE = "eth1.201"

# RDS CODER
COM_PORT_RDS = "/dev/ttyUSB4"
