import sys, os
from mivot_validator.utils.logger_setup import LoggerSetup

logger = LoggerSetup.get_logger()
LoggerSetup.set_debug_level()

logger.info("utils package initialized")
