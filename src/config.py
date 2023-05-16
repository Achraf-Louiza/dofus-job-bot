import platform
import string
import pytesseract

# from modules.logs.logs import Logs

# Get os type 
OS = platform.system()
OS_MAC = 'Darwin'
OS_WINDOWS = 'Windows'

# 
# Recoltable map positions file path-------------------------------------------------------------------
RECOLTABLE_MAP_BLUEPRINT_FILE_PATH =  "../data/recoltables_blueprint.csv"

# "Dofosdb" api url for web scraping recoltable map positions.
DOFUSDB_API_URL =  "https://api.dofusdb.fr/recoltable"
RECOLTABLE_NAME = 'wheat'
WHEAT_API_ID = 289
NMAX_RESPONSES = 91

# Recoltables
RECOLTABLE_NAMES = ['ble', 'avoine', 'houblon']
STR_RECOLTABLE_AVAILABLE = 'fauch'
STR_RECOLTABLE_UNAVAILABLE = 'puis'

# OCR list of characters to detect------------------------------------------------------------------------------------
ALPHABET_CHARS = string.ascii_lowercase + string.ascii_uppercase
COORDINATES_CHARS = '0123456789,-N'


# Move from map position to another : You can only move RIGHT, LEFT, UP, DOWN.--------------------
RIGHT = (0.1, 0.2)
LEFT = (0.05, 0.05)
DOWN = (0.1,0.2)
UP = (650, 30)

# Map position (width or height) percentage for box edges ----------------------------------------
P_MAP_LEFT = 0.01
P_MAP_TOP = 0.07
P_MAP_RIGHT = 0.05
P_MAP_BOTTOM = 0.1

# Near current pixel coordiantes -----------------------------------------------------------------
# Percentage for box edges
P_MOUSE_LEFT = 0.02
P_MOUSE_TOP = - 0.1
P_MOUSE_RIGHT = 0.15
P_MOUSE_BOTTOM = 0.02
# Box minimal (width, height) 
P_MOUSE_MIN_HEIGHT = 0
P_MOUSE_MAX_HEIGHT = 0 

# Game Usable ground box cooridnates -------------------------------------------------------------
# Percentage for box edges
P_GROUND_LEFT = 0
P_GROUND_TOP = 0
P_GROUND_RIGHT = 0
P_GROUND_BOTTOM =0
# Scanner percentage of inbetween edge size in the grid search
P_SCAN_X_SKIP = 0 
P_SCAN_Y_SKIP = 0

# Test variables
image_coords_path = '../data/images/coordinates_test.png'
image_near_cursor = '../data/images/near_cursor_test.png'
