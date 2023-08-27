import platform
import string
import pytesseract

# from modules.logs.logs import Logs

# Get os type 
OS = platform.system()
OS_WINDOWS = 'Windows'

# 
# Recoltable map positions file path-------------------------------------------------------------------
RECOLTABLE_MAP_BLUEPRINT_FILE_PATH =  "../data/recoltable_map_positions/recoltables_blueprint.csv"

# "Dofosdb" api url for web scraping recoltable map positions.
DOFUSDB_API_URL =  "https://api.dofusdb.fr/recoltable"
RECOLTABLE_NAME = 'wheat'
WHEAT_API_ID = 289
NMAX_RESPONSES = 91

# Recoltables
RECOLTABLE_NAMES = ['ble','wheat',  'avoine', 'houblon', 'seigle', 'lin', 'orge', 'riz', 'malt', 'chanvre', 'maïs', 'millet']
mapToRecoltable = {x:x for x in RECOLTABLE_NAMES}
mapToRecoltable['ble'] = 'wheat'
mapToRecoltable['bl\n'] ='wheat'
mapToRecoltable['bie'] = 'wheat'
STR_RECOLTABLE_AVAILABLE = 'fauch'
STR_RECOLTABLE_UNAVAILABLE = 'epuis'

# Recoltable pixel coordinates 
RECOLTABLE_PIXEL_COORDINATES = "../data/recoltable_pixel_coordinates/recoltable_pixel_coords.csv"

# OCR list of characters to detect------------------------------------------------------------------------------------
ALPHABET_CHARS = string.ascii_lowercase + string.ascii_uppercase + 'éèê'
COORDINATES_CHARS = '0123456789,-'

recoltablesPerChar = {'The-blood-omni': ['orge', 'wheat', 'ble', 'bie', 'bl\n'],
                      'Guelaa-tiempo': RECOLTABLE_NAMES,
                      'Chef-rox': ['wheat', 'ble', 'bie', 'bl\n']
                     }

# Move from map position to another : You can only move RIGHT, LEFT, UP, DOWN.--------------------
RIGHT = (0.81, 0.5)
LEFT = (0.18, 0.7)
DOWN = (0.4, 0.86)
UP = (0.7, 0.03)

# Map position (width or height) percentage for box edges ----------------------------------------
P_MAP_LEFT = 0.0061
P_MAP_TOP = 0.066
P_MAP_RIGHT = 0.067
P_MAP_BOTTOM = 0.1

# Near current pixel coordiantes -----------------------------------------------------------------
# Percentage for box edges
P_MOUSE_LEFT = 0.005
P_MOUSE_TOP = - 0.11
P_MOUSE_RIGHT = 0.115
P_MOUSE_BOTTOM = 0.019
# Box minimal (width, height)  / Unused currently
P_MOUSE_MIN_HEIGHT = 0
P_MOUSE_MAX_HEIGHT = 0 

# Game Usable ground box cooridnates -------------------------------------------------------------
# Percentage for box edges
P_GROUND_LEFT = 0.17
P_GROUND_TOP = 0.03
P_GROUND_RIGHT = 0.83
P_GROUND_BOTTOM =0.85
# Scanner percentage of inbetween edge size in the grid search
P_SCAN_X_SKIP = 0.035
P_SCAN_Y_SKIP = 0.035

# Test variables
image_coords_path = '../../data/images/coordinates_test.png'
image_near_cursor = '../../data/images/near_cursor_test.png'
image_clickable_zone = '../../data/images/clickable_zone.png'
