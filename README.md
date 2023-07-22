# DownloadTV

IMPORTANT: This tool does __**not**__ not work in its current state. I'm still looking for a TV-Porgram-Guide API. if you know any, please let my know, by opening an issue!

A tool that i (want to) use myself to record various freeTV shows via an onlinelivestream. This software may not work for all streams, since the implementations vary a lot.

## How should my config look like?

### EPG
currently only json guides from IPTv.Org are supported. I may add support for xml later on.

## Movies

You just need the exact name of the Movie / TV-Show. The Config does not need to be written case sensitive.


Example Config:

        {
            "log": true,
            "EPG": "https://iptv-org.github.io/epg/guides/de/magentatv.at.json",
            "Movies": {
                "Monk": true,
                "Harry Potter": false,
                "LordOfTheRings": true,
                "Nobody Home": true
            }
        }


## What streams are supported

This is a list of all working and tested streams as of 01/2023

- ZDF
- ZDF Neo
- ZDF Info
- Das Erste
- Basically most of the streams IPTv.Org supports

## My Stream doesn't work, can you fix it?

Maybe i can but i probably wont. I wrote this tool for myself. Others may use this tool **without any warranty**. If you want your stream to work, fork this repository and create a pull request, I'd be very happy to approve it.

## How to install

1. Clone repository
    git clone https://github.com/thegreatmisconception/RecordFreeNetworkIPTV

2. Install PIP-requirements
    pip install -r requirements.txt

## License

Licensed under MIT by TheGreatMisconception. See LICENSE file for more information


