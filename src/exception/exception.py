import sys  # For interacting with the system


class customexception(Exception):
    # init i sthe constructor
    def __init__(self,error_msg,error_detail:sys):
        self.error_message=error_msg
        _,_,exc_tb=error_detail.exc_info()  # Get the traceback information (none,none,none), first 2 ke no need
        print(exc_tb) #this means execution traceback

        self.lineno=exc_tb.tb_lineno  # Get the line number of the exception
        self.file_name=exc_tb.tb_frame.f_code.co_filename  # Get the file name of the exception


    def __str__(self):
        return "Error occured in python script name [{0}] line number [{1}] error message [{2}]".format(
        self.file_name, self.lineno, str(self.error_message))


if __name__ == "__main__":
    try:
        a = 1 / 0  # Example calculation (no error here)
    except Exception as e:
        # If an exception occurs, you can raise your custom exception here
        raise customexception(e, sys)
        # print(e)  # Print the original exception
        # print("error")
    # else:
    #     print("Execution successful. Result:", a)
