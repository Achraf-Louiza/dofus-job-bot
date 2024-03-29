import pyautogui
import win32gui
import numpy as np
import sys
sys.path.insert(0, '..')
import config, settings
from modules.monitor import Monitor
from modules.ocr import OCR
from modules.recoltable_scanner import RecoltableScanner
from modules.ui_handler import UIHandler
from PIL import Image
import unittest
import pytesseract
import time
from pathlib import Path

class TestUIHandler(unittest.TestCase):
    def __init__(self):
        self.monitor = Monitor(0)
        self.monitor.windows[0].focus()
        self.ocr = OCR()
        self.recoltable_scanner = RecoltableScanner()
        self.ui_handler = UIHandler(self.monitor, self.ocr, self.recoltable_scanner)
        
    def test_monitor_window_reading(self):
        character_name = 'The-blood-omni'
        dofus_window_title = self.monitor.windows[0].window.title
        self.monitor.windows[0].focus()
        assert character_name in dofus_window_title, f"Character {character_name} wasn't found in the first window!"
        print('TEST DOFUS WINDOW DETECTION OK!')
    
    def test_screenshot_map_position_img(self):
        screenshot = self.monitor.get_box_map_position()
        try:
            screenshot.save(config.image_coords_path)
            print('TEST SCREENSHOT MAP POSITION OK')
        except:
            print("Screenshot map position saving has failed!")
    
    def test_screenshot_infight_img(self):
        screenshot = self.monitor.get_box_infight()
        try:
            screenshot.save(config.image_coords_path)
            print('TEST SCREENSHOT INFIGHT OK')
        except:
            print("Screenshot INFIGHT saving has failed!")
        return screenshot
    
    def test_surrender_button_pos(self):
        self.ui_handler.click_on_pixel(self.monitor.width*settings.P_SURRENDER_X, self.monitor.height*settings.P_SURRENDER_Y)
        pyautogui.press('enter')
        time.sleep(1)
        self.ui_handler.click_on_pixel(self.monitor.width*settings.P_FREE_SPIRIT_YES_X, self.monitor.height*settings.P_FREE_SPIRIT_YES_Y)
        time.sleep(1)
        pyautogui.press('esc')
        self.ui_handler.click_on_pixel(self.monitor.width*settings.LEFT[0], self.monitor.height*settings.LEFT[1])
        time.sleep(3)
        self.ui_handler.click_on_pixel(self.monitor.width*settings.PHOENIX_X, self.monitor.height*settings.PHOENIX_Y)
        time.sleep(3)
        pyautogui.press('&')
        
    def measure(self, img1, img2):
        # Calculate Mean Squared Error (MSE)
        mae = np.mean(np.abs((img1 - img2)))
        # Normalize the MSE score between 0 and 1 (lower values indicate higher similarity)
        max_pixel_value = 255  # For grayscale images
        similarity_score = 1 - (mae / max_pixel_value)
        return similarity_score

    
    def test_screenshot_near_cursor_img(self):
        time.sleep(1)
        """seigle_x = 0.4 * self.monitor.width
        seigle_y = 0.35 * self.monitor.height"""
        seigle_x = 0.3 * self.monitor.width
        seigle_y = 0.3 * self.monitor.height
        self.monitor.move_cursor(seigle_x, seigle_y)
        time.sleep(1)
        screenshot, _ = self.monitor.get_box_near_cursor_position()
        try:
            screenshot = Image.fromarray(screenshot)
            screenshot.save(config.image_near_cursor)
            print('TEST SCREENSHOT NEAR CURSOR POSITION OK')
        except:
            print("Screenshot near cursor position saving has failed!")

    def test_screenshot_clickable_game_zone_img(self):
        screenshot = self.monitor.get_clickable_game_zone()
        try:
            screenshot.save(config.image_clickable_zone)
            print('TEST SCREENSHOT CLICKABLE GAME ZONE OK')
        except:
            print("Screenshot clickable game zone saving has failed!")
    
    def test_scan_map_recoltables(self):
        self.ui_handler.scan_map_recoltables(recolt = True)
        print('TEST RECOLTABLE SCANNER OK')
        
    def test_ocr(self):
        # Test coords OCR
        coords = [5, -25]
        coords = [f'{coords[0]},{coords[1]},', f'{coords[0]},{coords[1]}', f'{coords[0]}, {coords[1]}', f'{coords[0]}, {coords[1]},']
        test_img_coords = Image.open(config.image_coords_path)
        text = self.ocr.recognize_text(test_img_coords, config.COORDINATES_CHARS)
        text = text.strip('\n\s ')
        #assert text in coords, f"'{text}' is not in: {coords}"
        # Test recoltable OCR
        recoltable = 'seigle'
        test_near_cursor = Image.open(config.image_near_cursor)
        text = self.ocr.recognize_text(test_near_cursor, config.ALPHABET_CHARS).lower()
        assert recoltable in text, f"{recoltable} isn't included in : '{text}'"
        print('TEST OCR RECOGNIZE TEXT (coords + recoltable) OK!')
    
    def test_extract_map_position(self):
        coords = [5, -25]
        detected_coords = self.ui_handler.extract_current_map_position()
        print(detected_coords)
        assert detected_coords[0]==coords[0] and detected_coords[1]==coords[1], f'found coords: {detected_coords} are different from real coords {coords}'
        print('TEST EXTRACT MAP POSITION OK!')
    
    def test_elementary_blocks(self):
        self.test_monitor_window_reading()
        self.test_screenshot_map_position_img()
        self.test_screenshot_near_cursor_img()
        self.test_screenshot_clickable_game_zone_img()
        self.test_ocr()
        
    def test_basic_movement_coords(self):
        for pos in [config.RIGHT, config.LEFT, config.UP, config.DOWN]:
            self.monitor.move_cursor(pos[0]*self.monitor.width, pos[1]*self.monitor.height)
            time.sleep(1)
        print('TEST BASIC MOVEMENT COORDINATES OK')
        