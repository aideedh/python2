

# Custom exception class 
# - Inherited from Exception class
class IPException(Exception):

    # setting up exception init method
    # - passing the user input ip address
    def __init__(self, ipAddress):
        # making the custom error message
        super().__init__(f"Invalid IP address: {ipAddress}")
        self.ipAddress = ipAddress

