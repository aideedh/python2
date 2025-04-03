

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

    # user interactions
    def user():

        # original list
        credentials = []

        # get user inputs
        username = input("What is your username: ")
        password = input("What is your password? ")
        ip = input("What is your ip? ")

        # raise exception
        # - only if the ip validaton is met
        if validIp(ip) == False:
            raise IPException(ip)


        # put user inputs into list
        # - only if the exception is not raised
        info = [username, password, ip]

        # pass the list into original list of information
        # - this will be updated every time
        credentials.append(info)

    # check for ip address 
    def validIp(ipAddress):

        # split the segments in the ip address
        # - seprated by "."
        ipSegments = ipAddress.split(".")

        #----------------
        # ALL ip checks -
        #----------------------------------------------------------------------------------
        # If any of these are triggured it will return false and raise the custom exception
        #----------------------------------------------------------------------------------

        # check for if the segemnts in the ip address is 4
        if len(ipSegments) != 4:
            return False

        # check if segemnts in ip address is from 0 to 255
        for segment in ipSegments:
            try:
                num = int(segment)
                if num < 0 or num > 255:
                    return False
                
        # raise custom error all else
            except:
                return False
                
        

