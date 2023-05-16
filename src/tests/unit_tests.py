import pyautogui
import modules
import win32gui
import config
from modules.monitor import MonitorWindows
from modules.ocr import OCR
from PIL import Image
import unittest
import pytesseract
import time
from pathlib import Path
from tests.popup import open_popup_test_finished

def main():
    # UIHandler test
    uihandler_testor = TestUIHandler()
    uihandler_testor.test_monitor_window_reading()
    uihandler_testor.test_screenshot_map_position_img()
    uihandler_testor.test_screenshot_near_cursor_img()
    uihandler_testor.test_ocr()
    
    open_popup_test_finished()  
    
class TestUIHandler(unittest.TestCase):
    def __init__(self):
        pytesseract.pytesseract.tesseract_cmd = 'C://Program Files/Tesseract-OCR/tesseract.exe' 
        self.monitor = MonitorWindows(0)
    
    def test_monitor_window_reading(self):
        character_name = 'The-blood-omni'
        dofus_window_title = self.monitor.windows[0].window.title
        assert character_name in dofus_window_title, f"Character {character_name} wasn't found in the first window!"
        print('TEST DOFUS WINDOW DETECTION OK!')
    
    def test_screenshot_map_position_img(self):
        screenshot = self.monitor.get_box_map_position()
        try:
            screenshot.save(config.image_coords_path)
            print('TEST SCREENSHOT MAP POSITION OK')
        except:
            print("Screenshot map position saving has failed!")
    
    def test_screenshot_near_cursor_img(self):
        time.sleep(2)
        screenshot = self.monitor.get_box_near_cursor_position()
        try:
            screenshot = Image.fromarray(screenshot)
            screenshot.save(config.image_near_cursor)
            print('TEST SCREENSHOT NEAR CURSOR POSITION OK')
        except:
            print("Screenshot near cursor position saving has failed!")
       
    def test_ocr(self):
        ocr = OCR()
        # Test coords OCR
        coords = ['5,-25,', '5,-25', '5, -25', '5, -25,']
        test_img_coords = Image.open(config.image_coords_path)
        text = ocr.recognize_text(test_img_coords, config.COORDINATES_CHARS)
        text = text.strip('\n\s ')
        assert text in coords, f"'{text}' is not in: {coords}"
        # Test recoltable OCR
        recoltable = 'seigle'
        test_near_cursor = Image.open(config.image_near_cursor)
        text = ocr.recognize_text(test_near_cursor, config.ALPHABET_CHARS).lower()
        assert recoltable in text, f"{recoltable} isn't included in : '{text}'"
        print('TEST OCR RECOGNIZE TEXT (coords + recoltable) OK!')
    
    
        
# Run main
main()