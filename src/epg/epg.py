import requests
import json

class EPG():
    # Initialize the Class
    def __init__(self, stream, epg):
        self.guide_uri = epg
        self.stream_uri = stream
        
    # Get the EPG data
    def getGuide(self):
        try:
            guide = requests.get(self.guide_uri)
            guide = guide.json()
        except Exception as e:
            print(e)
            print("some problem occured while trying to download the guide.")
        return guide
    
    # Get channel information - adress resolution, etc...
    def getChannelInformation(self):
        try:
            channels = requests.get(self.stream_uri)
            channels = channels.json()
        except Exception as e:
            print(e)
            print("coudn't fetch channel list. Check Config or Internet Connection")
        return channels
    