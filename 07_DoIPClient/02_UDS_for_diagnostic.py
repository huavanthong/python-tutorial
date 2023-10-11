from doipclient.connectors import DoIPClientUDSConnector
from udsoncan.client import Client
from udsoncan.services import *

uds_connection = DoIPClientUDSConnector(client)
with Client(uds_connection) as uds_client:
    client.ecu_reset(ECUReset.ResetType.hardReset)