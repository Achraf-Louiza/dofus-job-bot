from config import UP, DOWN, RIGHT, LEFT
import config
import pyautogui
import numpy as np
<<<<<<< HEAD
import pandas as pd
from character import Character
from pathfinder import Pathfinder
from ocr import OCR
from recoltableScanner import RecoltableScanner
from monitor import MonitorWindows
from ui_handler import UIHandler
from action import Action, MoveTopMapPosition, ClickOnCoords, Recolt, ScanMapPosition
=======
from pathfinder import Pathfinder
>>>>>>> main

class Player:
    """
    A class representing a player controlling the champion in dofus
    
    """
    def __init__(self):
<<<<<<< HEAD
        
        # Part 1: Init characters ----------------------------------------------
        # Init uihandlers
        uihandlers = self._create_ui_handlers()
        # Init characters
        self.characterObjs = self._init_characters(uihandlers)
        
        # Part 2: Filter recoltable destinations for each character-------------
        # Init global recoltables coordinates
        self.map_blueprint = self._read_recoltable_coords()
        # Init characters individual destinations
        self.characters_destionations_coords = self._init_characters_destinations(map_blueprint)
=======
        pathfinder = Pathfinder()
        
        
>>>>>>> main
    
    def run_global_strategy(self):
        chars_i_destinations = [0 for _ in range(len(self.characterObjs))]
        chars_i_next_pixel_recolt = [0 for _ in range(len(self.chracterObjs))]
        while not self._has_compelted():
            for i, (character, destination) in enumerate(zip(self.characterObjs, self.characters_destionations_coords)):
                index_in_path = chars_i_destinations[i]
                next_destination = destination[index_in_path]
                if character.has_arrived(next_destination[0], next_destination[1]):
                    # Do you know the pixel coords for this map position ? 
                    pixel_coords = self.map_blueprint[(self.map_blueprint['map_x']==next_destination[0]) & (self.map_blueprint['map_y']==next_destination[1])]
                    if len(pixel_coords.dropna(subset=['pixel_x'])) != 0:
                        # RECOLT ONE BLOCK OF RECOLTABLE
                        # get recoltables pixel coords of the current map position
                        next_pixel_recolt = pixel_coords.values[chars_i_next_pixel_recolt[i]]
                        action = Recolt(next_pixel_recolt)
                        character.execute_action(action)
                        chars_i_next_pixel_recolt[i] += 1
                        if chars_i_next_pixel_recolt[i] == len(pixel_coords) - 1:
                            chars_i_destinations[i] += 1
                            chars_i_next_pixel_recolt[i] = 0
                    else:
                        # SCAN ALL THE GRID FOR THE CURRENT CHARACTER - others on hold
                        scan_action = ScanMapPosition(next_destination, self.map_blueprint)
                        self.map_blueprint = character.execute_action(scan_action)
                else:
                    # MOVE ONE STEP(RIGHT, LEFT, ...) TOWARDS the map position destination
                    move_action = MoveTopMapPosition(character.map_coords, destination[index_in_path])
                    character.execute_action(move_action)
                    
   
    def _has_completed(self):
        for i, destinations in enumerate(self.characters_destionations_coords):
            if not self.characterObjs[i].has_arrived(destinations[-1][0], destinations[-1][1]):
                return False
        return True
    
    def _read_recoltable_coords(self):
        df = pd.read_csv(config.RECOLTABLE_MAP_POSITIONS_FILE_PATH)
        return df
    
    def _create_ui_handlers(self):
        # Init OCR--------------------------------
        ocrObj = OCR()
        # Init Recoltable Scanner ----------------
        recoltableScannerObj = RecoltableScanner()
        # Init monitors --------------------------
        monitors = pyautogui.getMonitors()
        monitorObjs = [MonitorWindows(i) for i, monitor in enumerate(monitors)]
        # Init UIHandlers ------------------------
        uihandlers = [UIHandler(monitorObj, ocrObj, recoltableScannerObj) for monitorObj in monitorObjs]
        return uihandlers
    
    def _init_characters(self, uihandlers):
        characterObjs = []
        for uihandler in uihandlers:
            windows = uihandler.monitor.windows
            for window in windows:
                character_name = window.title.split('-')[0].strip()
                window.maximize()
                character = Character(window.id, character_name, 100, True, uihandler)
                characterObjs.append(character)
        return characterObjs
    
    def _init_characters_destinations(self, coords: pd.DataFrame) -> list:
        # To do: filter on subscription & level
        # We suppose all the characters have the same set of destinations
        
        # Characters sorted list of destinations
        destinations = [coords[['map_x', 'map_y']].drop_duplicates().values.tolist() for _ in range(len(self.characterObjs))]
        destinations = [self.pathfinderObj.shortest_path_nearest_neighbors(character.map_coords, destinations[i]) for i, character in enumerate(self.characterObjs)]
        return destinations
   