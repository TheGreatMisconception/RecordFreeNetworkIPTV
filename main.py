# Import all submodules
import src.config.config as cfg
import src.epg.epg as epg
import src.log.log as log


def main():
    # CLASS INIT
    config = cfg.CONFIG()
    guide_uri = config.getEPG()
    streams_uri = config.getStreams()
    # GET DATA
    #guide = epg.EPG(guide_uri,streams_uri)
    log.LOGGING(logging=True)
    



# Only if main.py is executed directly, call main method

if __name__ == "__main__":
    main()