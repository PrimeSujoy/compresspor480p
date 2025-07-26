from bot.get_cfg import get_config

class Config(object):
    # You can keep this default
    SESSION_NAME = get_config("SESSION_NAME", "EncoderX") 
    # EncoderX_bot....
    # sucks Dude
    APP_ID = int(get_config("APP_ID", "22182189"))
    API_HASH = get_config("API_HASH", "5e7c4088f8e23d0ab61e29ae11960bf5")
    LOG_CHANNEL = get_config("LOG_CHANNEL", "-1002872961182")
    UPDATES_CHANNEL = get_config("UPDATES_CHANNEL", "ProToppers") # Without `@` LOL
     # Get these values from my.telegram.org
    AUTH_USERS = [8181241262, -1002833051403, -1002762603310, -1002786441607, 5487643307, 7813152875, 8019639744, 7198013412, 6855989110, 7328629001, 1203096654, 6678172354, 1368753935, 1165873199]
# array , simplest method was AUTH_USERS = [] ; AUTH_USERS.append(your telegram id) 🌹
    TG_BOT_TOKEN = get_config("TG_BOT_TOKEN", "8024060891:AAHVlnrgbx3Ttme8pbzM0jUs7Y0tGrJJp0k")
    # the download location, where the HTTP Server runs
    DOWNLOAD_LOCATION = get_config("DOWNLOAD_LOCATION", "./downloads")
    # Telegram maximum file upload size
    BOT_USERNAME = get_config("BOT_USERNAME", "Compressor480p_Robot")
    MAX_FILE_SIZE = 4194304000
    TG_MAX_FILE_SIZE = 4194304000
    FREE_USER_MAX_FILE_SIZE = 4194304000
    # default thumbnail to be used in the videos
    DEF_THUMB_NAIL_VID_S = get_config("DEF_THUMB_NAIL_VID_S", "https://envs.sh/Lda.jpg")
    # proxy for accessing youtube-dl in GeoRestricted Areas
    # Get your own proxy from https://github.com/rg3/youtube-dl/issues/1091#issuecomment-230163061
    HTTP_PROXY = get_config("HTTP_PROXY", None)
    # maximum message length in Telegram
    MAX_MESSAGE_LENGTH = 4096
    # add config vars for the display progress
    FINISHED_PROGRESS_STR = get_config("FINISHED_PROGRESS_STR", "█")
    UN_FINISHED_PROGRESS_STR = get_config("UN_FINISHED_PROGRESS_STR", "▒")
    LOG_FILE_ZZGEVC = get_config("LOG_FILE_ZZGEVC", "Log.txt")
    SHOULD_USE_BUTTONS = get_config("SHOULD_USE_BUTTONS", False)
