class Result:
    """Represents the resultant data from a service check"""

    def __init___(self, status=False, error_msg="Check failed", details=[]):
        self.status    = status    #Boolean value for status of check
        self.error_msg = error_msg #error string to be returned
        self.details   = details   #List of strings with output & check details



