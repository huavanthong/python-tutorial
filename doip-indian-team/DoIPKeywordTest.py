"""
    File_name       :   DoIP_KeywordTest.py
    Class name      :   DoIP_KeywordTest
    Description     :   This File contains the class to send UDS message via DoIP Common Library
    Date        Version   Author             Comments
    **************************************************************************************
    12/16/2020  1.0       ala2cob            Initial Development
	20/1/2021	1.1		  myo1cob            CodeCleanup
    **************************************************************************************
"""
from InterfaceLib import InterfaceLib
from robot.api import logger
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword

__version__ = '1.0.0'

# The Keywords inside the class can be modified based on the project requirements

class DoIPKeywordTest(InterfaceLib):

    ROBOT_LIBRARY_VERSION = __version__
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
    
    """
    This Class contains keywords to test DoIP functionalities
    """
    @keyword("DoIP Initialize")
    def doip_initialize(self):
        self.doip_lib.doip_init()

    @keyword("DoIP Send Diag Message")
    def doip_send_diag_message(self, msg):
        payload, responses = self.doip_lib.send_diag_message(msg)
        logger.info(responses)
        return payload
    
    @keyword("DoIP Validate Diag Response")
    def doip_validate_diag_response(self, msg, from_position, to_position, validator,):
        '''
            This api should be adapted to proper slicing of message based on the 
            required validation
        '''
        i = int(from_position)
        j = int(to_position)
        if msg[i][:(j+1)] == validator:
            logger.info("The Message received : " + msg[0])
            logger.info("The Validator : " + validator)
            logger.info("The DoIP Message Validation Successful")
        else:
            logger.info("The Message received : " + msg[0])
            BuiltIn().fail("The DoIP Message Validation Failed")
    
    @keyword("DoIP Start Tester Present")
    def doip_start_tester_present(self, interval):
        self.doip_lib.begin_tester_present(interval)
    
    @keyword("DoIP Stop Tester Present")
    def doip_stop_tester_present(self):
        self.doip_lib.end_tester_present()
    
    @keyword("DoIP Disconnect")
    def doip_disconnect(self):
        self.doip_lib.doip_teardown()
        
