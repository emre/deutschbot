
# General Settings

NODES = ["https://api.steemit.com", "https://rpc.buildteam.io"]
DB_CONNECTION_URI = "mysql+pymysql://root:pass@localhost/germanybot"
BOT_TOKEN = "discord.bot_token"

# Curation settings

BOT_ACCOUNT = "turbot"
BOT_POSTING_KEY = "private wif"
TAGS = ["deutsch"]
HOOKS = [
    "https://discordapp.com/api/webhooks/410134452698611712/XVxNyJnVUJjDTfUL99N3i2oZzvQEhTpeWs1FRlI3sTiny6eykO3dQkARoQfWTDw63yGD",
    "https://discordapp.com/api/webhooks/410134521053315093/4M2Pv8u2j5BE08lmtmR4ZzbZkPyxSwP1Zuc6PMiasv7R5qZ8flxPI2gCVsc5mfXDj2n5"
]

#  option ids (no need to edit)
THRESHOLD_OPTION_ID = 1
LAST_BLOCK_ID = 2

try:
    from . local_settings import *
except ImportError:
    pass
