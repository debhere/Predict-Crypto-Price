import sys
from src.predictcrypto.logger import logging

def exception_details(error:Exception, trace:sys) -> str:
    _,_, exc = trace.exc_info()
    filename = exc.tb_frame.f_code.co_filename

    error_details = f"Error occured in {filename} in line no. {exc.tb_lineno} : {str(error)}"
    
    logging.info(error_details)
    return error_details

class CustomException(Exception):
    def __init__(self, error: Exception, trace: sys):
        super().__init__(error)
        self.trace = exception_details(error, trace)

    def __str__(self):
        return self.trace