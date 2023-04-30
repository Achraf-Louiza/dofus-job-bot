import platform
from modules.logs.logs import Logs

# Get os type 
OS = platform.system()
OS_MAC = 'Darwin'
OS_WINDOWS = 'Windows'

# Wheat map positions file path
RECOLTABLE_MAP_POSITIONS_FILE_PATH = lambda recoltable: f"../data/{recoltable}_map_positions.csv"

# "Dofosdb" api url for web scraping recoltable map positions.
DOFUSDB_API_URL =  "https://api.dofusdb.fr/recoltable"
RECOLTABLE_NAME = 'wheat'
WHEAT_API_ID = 289
NMAX_RESPONSES = 91

# Move from map position to another : You can only move RIGHT, LEFT, UP, DOWN.
RIGHT = (1103, 389)
LEFT = (194, 358)
DOWN = (650,680)
UP = (650, 30)


# Logs object instance
LOGS = Logs()
