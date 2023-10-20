import os

BOT_TOKEN = os.environ.get("BOT_TOKEN", "5222572158:AAENHtTOnhWBh4UUZKTjq5ruMtil_4zRA_0")
API_ID = int(os.environ.get("API_ID", "8858279"))
API_HASH = os.environ.get("API_HASH", "ef28c3f458143cbcb4271a98a2e9d596")
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001841958077"))
AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "5894098166").split())
DB_URL = os.environ.get("DB_URL", "mongodb+srv://480p:encode@cluster0.7fgwrif.mongodb.net/?retryWrites=true&w=majority")
DB_NAME = os.environ.get("DB_NAME", "BroadcastBot")
BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", True))
