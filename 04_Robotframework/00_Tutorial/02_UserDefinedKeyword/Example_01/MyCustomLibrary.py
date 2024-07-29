from robot.api import logger

def my_custom_keyword(arg1, arg2):
    """This is a custom keyword."""
    logger.info(f"Argument 1: {arg1}")
    logger.info(f"Argument 2: {arg2}")
