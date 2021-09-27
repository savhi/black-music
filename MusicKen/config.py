import os
from os import getenv

from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

que = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME")
ARQ_API_KEY = getenv("ARQ_API_KEY", None)
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "codersUpdates")
BG_IMAGE = getenv("BG_IMAGE", "https://telegra.ph/file/3e2bb945d7c90f0309eb8.png")
admins = {}
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
BOT_USERNAME = getenv("BOT_USERNAME")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "FlashProSpeed")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "codersSupport")
PROJECT_NAME = getenv("PROJECT_NAME", "BLACK MUSIC")
OWNER = getenv("OWNER", "@FlashProSpeed")
SOURCE_CODE = getenv("SOURCE_CODE", "github.com/Randi356/black-music")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "7"))
PMPERMIT = getenv("PMPERMIT", None)
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())

SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
KENKAN = getenv("KENKAN", "https://telegra.ph/file/fc74c34a8785c62eac0e1.png")
