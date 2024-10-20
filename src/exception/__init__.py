import os, sys

class CustomException(Exception):
    """
    A custom exception class that provides detailed error information.
    """

    def __init__(self, error_message:Exception, error_detailes: sys):
        """
        Initialize the CustomException with error message and details.
        """

        self.error_message = CustomException.get_detailed_error_message(error_message = error_message,
                                                                        error_detailes = error_detailes)
        
# try ->
# exception ->
# a, b, c = 1, 2, 3
# _, _, c
    @staticmethod
    def get_detailed_error_message(error_message:Exception, error_detailes: sys)->str:
        """
        Generate a detailed error message with additional context.
        """
        _, _, exce_tb = error_detailes.exc_info()

        # Extract relevant information from the traceback
        exception_block_line_number = exce_tb.tb_frame.f_lineno
        try_block_line_number = exce_tb.tb_lineno
        file_name = exce_tb.tb_frame.f_code.co_filename

        # Format the detailed error message
        error_message = f"""
        Error occured in execution of :
        [{file_name}] at
        try block line number : [{try_block_line_number}]
        and exception block line number : [{exception_block_line_number}]
        error message :[{error_message}]
        """
        return error_message
    
    def __str__(self):
        """
        Return a string representation of the CustomException.
        """
        return self.error_message
    
    def __repr__(self):
        """
        Return a string representation of the CustomException class.
        """
        return CustomException.__name__.str()
    