import json
import os

class CONFIG():
    # Initilize Config Class
    def __init__(self, **kwargs):
        # Use a custom path if specified else use generic
        if "path" in kwargs:
            self.path = kwargs["path"]
        else:
            self.path = os.getcwd()+"/config.json"

    def readConfig(self):
        # Check if file exists
        if os.path.exists(self.path):
            with open(self.path, "r") as file:
                config = file.read()
            # Check if the config contains valid json code and convert it to a python dict
            try:
                config = json.loads(config)
            except:
                print("Not Valid json, check syntax")
        else:
            # Replace print with logging
            print("Are you sure this file exists?")
            exit(0)
            
        return config


    # Return a array of Movies/Shows to record
    def getMovieList(self):
        # Only get Movies
        movielist = self.readConfig()["Movies"]

        # return array of Movies/Shows
        return movielist
    
    # Return a copy of the EPG Endpoint URL
    def getEPG(self):
        # Only get EPG Url
        epg_url = self.readConfig()["EPG"]
        
        # return url string
        return epg_url
    
    def getStreams(self):
        # Only get stream url
        streams = self.readConfig()["Streams"]
        
        # return url for information about the channels
        return streams
    
    