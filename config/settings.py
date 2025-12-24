import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

SERVER_ID = int(os.getenv("SERVER_ID"))
TICKET_CHANNEL_ID = int(os.getenv("TICKET_CHANNEL_ID"))
LOG_CHANNEL_ID = int(os.getenv("LOG_CHANNEL_ID"))
STAFF_ROLE_ID = int(os.getenv("STAFF_ROLE_ID"))

PREFIX = os.getenv("PREFIX", "$")

DB_FILE = "tickets.json"
COLOR = 0xEEC66D