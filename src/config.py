import platform
import string
import pytesseract

# from modules.logs.logs import Logs

# Get os type 
OS = platform.system()
OS_WINDOWS = 'Windows'

# 
# Recoltable map positions file path------------------------------------------------------------------------------------------------
RECOLTABLE_MAP_BLUEPRINT_FILE_PATH =  "../data/recoltable_map_positions/recoltables_blueprint.csv"
# Recoltable pixel coordinates 
RECOLTABLE_PIXEL_COORDINATES = "../data/recoltable_pixel_coordinates/recoltable_pixel_coords.csv"

# Recoltables ----------------------------------------------------------------------------------------------------------------------
RECOLTABLE_NAMES = ['ble','wheat',  'avoine', 'houblon', 'seigle', 'lin', 'orge', 'riz', 'malt', 'chanvre', 'maïs', 'millet']
mapToRecoltable = {x:x for x in RECOLTABLE_NAMES}
mapToRecoltable['ble'] = 'wheat'
STR_RECOLTABLE_AVAILABLE = 'fauch'
STR_RECOLTABLE_UNAVAILABLE = 'epuis'
recoltablesPerChar = {'The-blood-omni': ['orge', 'wheat', 'ble'],
                      'Guelaa-tiempo': RECOLTABLE_NAMES,
                      'Chef-rox': ['wheat', 'ble']
                     }
zoneAffectation = {'Guelaa-tiempo': 'bonta',
                   'The-blood-omni': 'astrub'}

# OCR list of characters to detect-------------------------------------------------------------------------------------------------------
ALPHABET_CHARS = string.ascii_lowercase + string.ascii_uppercase + 'éèê'
COORDINATES_CHARS = '0123456789,-'


# "Dofosdb" api url for web scraping recoltable map positions.------------------------------------------------------------------------
DOFUSDB_API_URL =  "https://api.dofusdb.fr/recoltable"
RECOLTABLE_NAME = 'wheat'
RECOLTABLE_IDS = {'wheat': 289, 'chanvre': 425, 'seigle': 532, 'lin': 423, 'malt': 405, 'orge': 400, 'avoine': 533, 'houblon': 401, 'riz': 7018}
NMAX_RESPONSES = {'wheat': 91, 'chanvre': 11, 'seigle': 21, 'lin': 21, 'malt': 11, 'orge': 41, 'avoine': 41, 'houblon': 21, 'riz': 11}


# Test variables-----------------------------------------------------------------------------------------------------------------------
image_coords_path = '../../data/images/coordinates_test.png'
image_near_cursor = '../../data/images/near_cursor_test.png'
image_clickable_zone = '../../data/images/clickable_zone.png'