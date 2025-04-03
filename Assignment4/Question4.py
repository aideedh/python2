

# Custom exception class 
# - Inherited from Exception class
class IPException(Exception):

    # setting up exception init method
    # - passing the user input ip address
    def __init__(self, ipAddress):
        # making the custom error message
        super().__init__(f"Invalid IP address: {ipAddress}")
        self.ipAddress = ipAddress



class Program:

    # user interactions
    def user(self):

        # original list
        credentials = []

        # get user inputs
        print(" ")
        print("Please enter your information:")
        username = input("What is your username: ")
        password = input("What is your password? ")
        ip = input("What is your ip? ")
        print(" ")


        # raise exception
        # - only if the ip validaton check is triggured
        if self.validIp(ip) == False:
            raise IPException(ip)


        # put user inputs into list
        # - only if the exception is not raised
        info = [username, password, ip]

        # pass the list into original list of information
        # - this will be updated every time
        credentials.append(info)


        # write to the file
        with open("SessionLogger.txt", "a") as file:
            for info in credentials:
                # this will format the informtion given in the desired format
                file.write(f'["{info[0]}","{info[1]}","{info[2]}"]\n')

        print("Editing file ... .. .")
        print("Process completed .. .")
        print("File has been updated!")

    # check for ip address 
    def validIp(self, ipAddress):

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
                

user = Program()
user.user()