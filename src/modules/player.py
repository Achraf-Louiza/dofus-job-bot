from config import UP, DOWN, RIGHT, LEFT
import pyautogui
import numpy as np
from screenshot_handler import ScreenshotHandler
from character import Character

class Player:
    """
    A class representing a player controlling the champion in dofus
    
    """
    def __init__(self, monitor_id: int = 0, n_accounts: int = 1) -> None:
        # Map & pixel coords
        self.map_x, self.map_y = None, None
        self.pixel_x, self.pixel_y = None, None
        # Monitor ID
        self.monitor_id = monitor_id
        # Screenshot handler
        self.screenshot = ScreenshotHandler(monitor_id)
        # Number of accounts 
        self.n_accounts = n_accounts
        # Characters 
        self.characters = self.create_characters()
    
    def _read_destination_coords(self):
        pass
   
    def _init_characters(self):
        pass

    def _read_characters_destinations_coords(self):
        pass

    def run_strategy(self, actionList: Action):
        pass