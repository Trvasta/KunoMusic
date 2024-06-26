import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("27497317"))
API_HASH = getenv("912dc329039f9fcf92b6ace0efb35cef")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("7221149690:AAGspc1Dw2mnrVqJg1on6bQJPU2IzO5aq00")

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("mongodb+srv://OrboroBot:OrboroBot@cluster0.tvxqfcx.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0", None)

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 300))

# Chat id of a group for logging bot's activities
LOGGER_ID = int(getenv("-1002207392342", None))

# Get this value from @FallenxBot on Telegram by /id
OWNER_ID = int(getenv("6484740378"))

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("orborobot")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HRKU-2c5ef219-3ac7-4908-b6cf-d2b12e44bf8f")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/aashuxxD/KunoMusic",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/DigiWebbing")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/OrboroBotSupport")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", true))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 204857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 2073741824))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from @StringFatherBot on Telegram
STRING1 = getenv("BQGjk2UAiGhHOr0X4yNyf_5Gauidsw1v4hdZ1hKXH-lQMJQBsYxDE7frTKS0hYzRu-8UoWGlaHcQBnmhhDl15xEcoN347VLMnvANTonleDeUnpYoZe0jkdu9ZP96u-u-KlUAVJ_CiAsXmxBwojjckTVmyw3nEBnq_ZUehC42V6Z23nOiYiOu2RxtgCMLlsgZNiAKiFeJsbyiaZoMMz4detZkw_zDivJKoKZzK8aWrZAVYgXgSYl5qX33XmJU3dvvSA9hFf31EPLHpDqBfSjrRxbd2ckN_wv6ucGJbBlu9qquSMRwkGXlDtI63_5XURA8CPz_SRRDWWiaIasZJn4u-dHZ9lPcogAAAAGChUkaAA", None)
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = ["https://te.legra.ph/file/5fd13f2cc0d03bce9f7f2.jpg",
                 "https://te.legra.ph/file/c15d01b3e6b40ea141dc9.jpg",
                 "https://te.legra.ph/file/58b491b39cee854695fa9.jpg"]
    
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://mallucampaign.in/images/img_1692101295.jpg"
)
PLAYLIST_IMG_URL = "https://graph.org/file/c95a687e777b55be1c792.jpg"
STATS_IMG_URL = "https://mallucampaign.in/images/img_1694847936.jpg"
TELEGRAM_AUDIO_URL = "https://graph.org/file/ff2af8d4d10afa1baf49e.jpg"
TELEGRAM_VIDEO_URL = "https://graph.org/file/ff2af8d4d10afa1baf49e.jpg"
STREAM_IMG_URL = "https://graph.org/file/ff2af8d4d10afa1baf49e.jpg"
SOUNCLOUD_IMG_URL = "https://graph.org/file/c95a687e777b55be1c792.jpg"
YOUTUBE_IMG_URL = "https://graph.org/file/e8730fdece86a1166f608.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://graph.org/file/0bb6f36796d496b4254ff.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://graph.org/file/0bb6f36796d496b4254ff.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://graph.org/file/0bb6f36796d496b4254ff.jpg"



def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:360"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
