import pyautogui
import win32gui
import sys
sys.path.insert(0, '..')
import config
from monitor import MonitorWindows
from ocr import OCR
from PIL import Image
import unittest
import pytesseract
import time
from pathlib import Path

def main():
    uihandler_testor = TestUIHandler()
    uihandler_testor.test_monitor_window_reading()
    uihandler_testor.test_screenshot_map_position()
    uihandler_testor.test_ocr()
    
class TestUIHandler(unittest.TestCase):
    def __init__(self):
        pytesseract.pytesseract.tesseract_cmd = 'C://Program Files/Tesseract-OCR/tesseract.exe' 
    
    def test_monitor_window_reading(self):
        character_name = 'The-blood-omni'
        self.monitor = MonitorWindows(0)
        dofus_window_title = self.monitor.windows[0].window.title
        assert character_name in dofus_window_title, f"Character {character_name} wasn't found in the first window!"
        print('TEST DOFUS WINDOW DETECTION OK!')
    
    def test_screenshot_map_position(self):
        screenshot = self.monitor.get_box_map_position()
        try:
            screenshot.save(config.image_coords_path)
            print('TEST SCREENSHOT MAP POSITION OK')
        except:
            print("Screenshot has failed!")
        
    def test_ocr(self):
        coords = ['5,-25,', '5,-25', '5, -25', '5, -25,']
        ocr = OCR()
        test_img_coords = Image.open(config.image_coords_path)
        text = ocr.recognize_text(test_img_coords, config.COORDINATES_CHARS)
        text = text.strip('\n\s ')
        assert text in coords, f"'{text}' is not in: {coords}"
        print('TEST OCR RECOGNIZE TEXT OK!')
        
        
        
main()