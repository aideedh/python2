

# Custom exception class 
# - Inherited from Exception class
class IPException(Exception):

    # setting up exception init method
    # - passing the user input ip address
    def __init__(self, ipAddress):
        # making the custom error message
        super().__init__(f"Invalid IP address: {ipAddress}")
        self.ipAddress = ipAddress



class program:

    def user():

        credentials = []


        username = input("What is your username: ")
        password = input("What is your password? ")

        ip = input("What is your ip? ")


        credentials = [username, password, ip]


        pass

    def validIp(ipAddress):
        pass

        

