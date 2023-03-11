import datetime
import os

class LOGGING():
    def __init__(self, **kwargs):
        if "logging" in kwargs:
            self.logging = kwargs["logging"]
        if "path" in kwargs:
            self.path = kwargs["path"]
        else:
            self.path = os.getcwd()+"/log.txt"
            print(self.path)
    
    # Check if logging is active
    def isLogging(self):
        if self.logging == True:
            return True
        else:
            return False
        
    
    def printLog(self, message):
        print(message)
    
    # Write to Logfile
    def writeLog(self, message):
        if self.isLogging():
            self.printLog(message)
            try:
                with open(self.path, "ab") as file:
                    file.write(message)
            except Exception as e:
                print(e)
                
    def warning(self, warning):
        warning = f"{datetime.datetime.now()} [WARNING] {warning}"
        self.writeLog(warning)
    
    def error(self, erorr):
        error = f"{datetime.datetime.now()} [ERROR] {error}"
        self.writeLog(error)
    
    def information(self, information):
        information =  f"{datetime.datetime.now()} [INFORMATION] {information}"
        self.writeLog(information)

                

            
        