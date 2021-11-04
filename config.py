import os
import aiohttp
from Python_ARQ import ARQ
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
ARQ_API_KEY = getenv("ARQ_API_KEY")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME", "Eagle")
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
OWNER_NAME = getenv("OWNER_NAME", "Manusiabajingann")
ALIVE_NAME = getenv("ALIVE_NAME", "ᴇᴀɢʟᴇ")
BOT_USERNAME = getenv("BOT_USERNAME", "Eagle_Xrobot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "EagleAssistant")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "Mutualan_Cari_Teman")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "infobotrelax")
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ? .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/52b399f7e7cc2d982e7e2.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/d6f92c979ad96b2031cba.png")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/6213d2673486beca02967.png")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/f02efde766160d3ff52d6.png")
IMG_4 = getenv("IMG_4", "https://telegra.ph/file/19ef76c0a097b1a394b00.png")

aiohttpsession = aiohttp.ClientSession()
arq = ARQ("https://thearq.tech", ARQ_API_KEY, aiohttpsession)
