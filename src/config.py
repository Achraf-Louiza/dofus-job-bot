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

# Test variables
image_coords_path = '../../data/images/coordinates_test.png'
image_near_cursor = '../../data/images/near_cursor_test.png'
image_clickable_zone = '../../data/images/clickable_zone.png'
