from .monitor import Monitor
from .ocr import OCR
from .recoltable_scanner import RecoltableScanner
import sys, os
from PIL import Image
from unidecode import unidecode
sys.path.insert(1, os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))) ; import config

class UIHandler:
    
    def __init__(self, monitor: Monitor, ocr: OCR, scanner: RecoltableScanner):
        self.monitor = monitor
        self.ocr = ocr
        self.scanner = scanner
    
    def focus_on_character(self, character_id: int):
        self.monitor.focus_on_window(character_id)
    
    def click_on_pixel(self, coord_x: int, coord_y: int):
        self.monitor.move_cursor(coord_x, coord_y)
        self.monitor.click_on_mouse()
    
    def extract_current_map_position(self) -> list:
        """
        Extract current dofus character's map position
        
        Returns
        -------
        str
            Text containing current map position    
        """
        screenshot = self.monitor.get_box_map_position()
        text = self.ocr.recognize_text(screenshot, config.COORDINATES_CHARS)
        coords = self.parse_map_position(text)
        return coords
    
    def extract_text_near_cursor(self) -> str:
        """
        Extract text in dofus inside a box (pop up) near current mouse pixel coordinates
        
        Returns
        -------
        str
            Text near mouse current pixel coordinates
        
        """
        screenshot, _ = self.monitor.get_box_near_cursor_position()
        screenshot = Image.fromarray(screenshot)
        text = self.ocr.recognize_text(screenshot, config.ALPHABET_CHARS)
        # Remove (accents)
        text = unidecode(text.lower())
        return text
    
    def scan_map_recoltables(self, map_pos: list, recolt: bool = True):
        self.scanner.init_grid_search(self.monitor)
        df = self.scanner.scan_grid(map_pos, self.monitor, self.ocr, recolt=recolt)
        return df
    
    def parse_map_position(self, text: str) -> list:
        """
        Parses map position from pytesseract OCR result 

        Parameters
        ----------
        text : str
            Text potentially contianing map coordinates [x, y] where x, y [-oo, +oo]

        Returns
        -------
        list
            A list of map position cooridnates [x, y] or an empty list [] if the parsing fails

        """
        # If comma was forgoten before a dash (negative value) Then we add it
        for i, char in enumerate(text):
            if i!=0 and char=='-':
                if text[i-1] != ',':
                    text = text[:i] + ',' + text[i:]
        # Get rid of all what comes after a second comma
        if len(text.split(','))>2:
            text = ','.join(text.split(',')[:2])
        # Strip alphabetical characters from the (beginning & end) of text and [, \n]
        text = text.strip('[, \n]'+config.ALPHABET_CHARS)
        # Extract coordinates
        try:
            coords = text.split(',')
            coords = [int(coord) for coord in coords]
            return coords
        except:
            return []
