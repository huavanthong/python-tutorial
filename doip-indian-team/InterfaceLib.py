from robot.libraries.BuiltIn import BuiltIn


class InterfaceLib(object):


    @property
    def doip_lib(self):
        BuiltIn().import_library('DoIPLibrary.py')
        return BuiltIn().get_library_instance("DoIPLibrary")
    