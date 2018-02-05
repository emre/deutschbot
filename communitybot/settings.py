
# General Settings

NODES = ["https://api.steemit.com", "https://rpc.buildteam.io"]
DB_CONNECTION_URI = "mysql+pymysql://root:yemre@localhost/germanybot"
BOT_TOKEN = "NDEwMDQyMjA0NDU5ODkyNzM4.DVnZPQ.vTJzHcsjSa92hQwNEZjwdKjpZ4E"

# Curation settings

BOT_ACCOUNT = "turbot"
BOT_POSTING_KEY = "private wif"
TAGS = ["deutsch"]
HOOKS = [
    "https://discordapp.com/api/webhooks/410134452698611712/XVxNyJnVUJjDTfUL99N3i2oZzvQEhTpeWs1FRlI3sTiny6eykO3dQkARoQfWTDw63yGD",
    "https://discordapp.com/api/webhooks/410134521053315093/4M2Pv8u2j5BE08lmtmR4ZzbZkPyxSwP1Zuc6PMiasv7R5qZ8flxPI2gCVsc5mfXDj2n5"
]

# you can give direct block id like 123123123 if not keep it like that and it
# will always start from the last_processed_block marked at the database.
START_BLOCK = "LAST_PROCESSED_BLOCK"

#  option ids (no need to edit)
THRESHOLD_OPTION_ID = 1
LAST_BLOCK_ID = 2

try:
    from local_settings import *
except ImportError:
    pass