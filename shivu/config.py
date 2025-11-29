class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    OWNER_ID = "7487670897"
    sudo_users = "7990456522", "7487670897", "8021397962"
    GROUP_ID = -1003410483524
    TOKEN = ""
    mongo_url = "mongodb+srv://WaifuXHusbandoCatcher:WaifuXHusbandoCatcher@cluster0.lnygfjx.mongodb.net/?appName=Cluster0"
    PHOTO_URL = ["https://graph.org/file/832d9e63f34f96a335c9d-2711fe9b1c754b3c94.jpg", "https://graph.org/file/0a8e66a00cd44c7315c42-b6e1ced788d13ccded.jpg"]
    SUPPORT_CHAT = "Gossip_Devil_Hub"
    UPDATE_CHAT = "Destiny_Infinity_Og"
    BOT_USERNAME = "Queen_Medusa_Catcher_Bot"
    CHARA_CHANNEL_ID = "-1003449944691"
    api_id = 27209067
    api_hash = "0bb2571bd490320a5c9209d4bf07902e"

    
class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
