from monitor import Monitor
from ocr import OCR
from recoltable_scanner import RecoltableScanner
import sys, os
sys.path.insert(1, os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))) ; import config

class UIHandler:
    
    def __init__(self, monitor: Monitor, ocr: OCR, scanner: RecoltableScanner):
        self.monitor = monitor
        self.ocr = ocr
        self.scanner = scanner
    
    def focus_on_character(self, character_id: int):
        self.monitor.focus_on_window(character_id)
    
    def click_on_pixel(self, coord_x: int, coord_y: int):
        self.monitor.click_on_mouse(coord_x, coord_y)
    
    def extract_current_map_position(self, character_id: int) -> list:
        """
        Extract current dofus character's map position
        
        Returns
        -------
        str
        Text containing current map position    
        """
        self.focus_on_character(character_id)
        screenshot = self.screenshot_handler.get_box_map_position()
        text = self.recognize_text(screenshot, config.COORDINATES_CHARS)
        coords = self.parse_map_position(text)
        return coords
    
    def extract_text_near_cursor(self, character_id: int) -> str:
        """
        Extract text in dofus inside a box (pop up) near current mouse pixel coordinates
        
        Returns
        -------
        str
        Text near mouse current pixel coordinates
        
        """
        self.focus_on_character(character_id)
        screenshot = self.screenshot_handler.get_box_near_cursor_position()
        text = self.recognize_text(screenshot, config.ALPHABET_CHARS)
        return text
    
    def scan_map_recoltables(self, character_id: int):
        self.focus_on_character(character_id)
        self.scanner.init_grid_search(self.monitor)
        self.scanner.scan_grid(self.monitr, self.ocr, recolt=True)