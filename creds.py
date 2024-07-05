import os
#from dotenv import load_dotenv, find_dotenv

#load_dotenv(find_dotenv())


class Credentials:
    BOT_TOKEN = os.environ.get("6369515689:AAEuEsp028Z2TF7PRqYIU6nfTNNw_KXbC54")  # from @botfather
    API_ID = int(os.environ.get("23210559"))  # from https://my.telegram.org/apps
    API_HASH = os.environ.get("bafc905bb83a29fd53f44f276c222a14")  # from https://my.telegram.org/apps
    # Banned Unwanted Members..
    BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS","").split())

# Okay 🤣
