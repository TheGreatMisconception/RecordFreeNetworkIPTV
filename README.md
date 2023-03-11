# DownloadTV

IMPORTANT: This tool does __**not**__ not work in its current state. 

A tool that i use myself to record various freetv shows via a onlinelivestream. This software may not work for all streams, since the implementations vary a lot.

## How should my config look like?

### EPG
currently only json guides from IPTv.Org are supported. I may add support for xml later on.

## Movies

You just need the exact name of the Movie / Show. The Config does not need to be written case sensitive.


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

## How to contribute

Fork, Code, Pull-request, Approve. **Everyone can learn to code**, but not everybody wants to :)

## License

Licensed under MIT by TheGreatMisconception. See LICENSE file for more information


