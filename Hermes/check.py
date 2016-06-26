class Check:
    """The base class for a check in the Hermes system"""

    def __init___(self, check_name='', target_ip='127.0.0.1', \
                    target_port='', target_proto='', \
                    timeout=15, jitter=15):
        self.check_name    = check_name   #Human readable id of the check
        self.target_ip     = target_ip    #Host server runs on
        self.target_port   = target_port  #Port to connect to
        self.target_proto  = target_proto #TCP, UDP, ICMP, etc
        self.timeout       = timeout      #time to run the check in seconds
        self.jitter        = jitter       #Percent value of self.timeout

    def do_check():
        """Performs the check and returns a Result object"""
        return Result()
