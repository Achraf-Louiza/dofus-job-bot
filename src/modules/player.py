from config import UP, DOWN, RIGHT, LEFT
import config
import pyautogui
import numpy as np
import pandas as pd
from .character import Character
from .pathfinder import Pathfinder
from .ocr import OCR
from .recoltable_scanner import RecoltableScanner
from .monitor import MonitorWindows
from .ui_handler import UIHandler
from .action import Action, MoveToMapPosition, ClickOnCoords, Recolt, ScanMapPosition
from .pathfinder import Pathfinder
import screeninfo
import time

class Player:
    """
    A class representing a player controlling the champion in dofus
    
    """
    def __init__(self):
        
        # Part 1: Init characters ----------------------------------------------
        # Init uihandlers
        uihandlers = self._create_ui_handlers()
        # Init characters
        self.characterObjs = self._init_characters(uihandlers)
        
        # Part 2: Filter recoltable destinations for each character-------------
        # Init global recoltables coordinates
        self.map_blueprint = self._read_recoltable_coords()
        # Init characters individual destinations
        self.pathfinderObj = Pathfinder()
        self.characters_destinations_coords = self._init_characters_destinations(self.map_blueprint)
        try:
            self.pixel_coords = pd.read_csv(config.RECOLTABLE_PIXEL_COORDINATES)
            # Temporary
            self.char_pixel_coords =[self.pixel_coords, self.pixel_coords]
            if len(self.pixel_coords)!=0:        
                for i, char in enumerate(self.characterObjs):
                    self.char_pixel_coords[i] = self.pixel_coords[self.pixel_coords.recoltable.map(lambda x: x in config.recoltablesPerChar[char.name])]
        except:
            self.pixel_coords = pd.DataFrame(columns=['recoltable', 'x', 'y', 'pixel_x', 'pixel_y'])
            self.char_pixel_coords =[self.pixel_coords, self.pixel_coords]

        # FINAL PART: Run global strategy
        self.run_recolting_strategy()
        
    
    def run_recolting_strategy(self):
        chars_i_destinations = [0 for _ in range(len(self.characterObjs))]
        chars_i_next_pixel_recolt = [0 for _ in range(len(self.characterObjs))]
        recolt_time = [0 for _ in range(len(self.characterObjs))]
        recolted = False
        last_action = ['None' for _ in range(len(self.characterObjs))]
        n_wait = 0
        next_destination = self.characters_destinations_coords[0][chars_i_destinations[0]]
        while not self._has_completed():
            for i, (character, destination) in enumerate(zip(self.characterObjs, self.characters_destinations_coords)):
                character.ui_handler.focus_on_character(character.id)
                time.sleep(1)
                print('----------------------------------------------------------')
                print(f'I am here {character.map_coords}')
                # Updating states -------------------------------------------------------------------------------------
                
                print(f'- last action: {last_action[i]}')
                if last_action[i] == 'move' :
                    if character.has_moved():
                        character.update_map_coords()
                        print(f'HAS MOVED TO {character.map_coords}')
                        print('State updating ...')
                    else:
                        print('Wainting for last movement to complete')
                        n_wait+=1
                        if n_wait == 20//len(self.characterObjs):
                            move_action = MoveToMapPosition(character.map_coords, next_destination)
                            character.execute_action(move_action)
                            n_wait = 0
                        continue
                elif last_action[i] == 'recolt':
                   if recolted:
                       if (time.time()-recolt_time[i]) < 3:
                           continue
                       if chars_i_next_pixel_recolt[i] == len(self.char_pixel_coords[i]) - 1:
                           recolted = False
                           continue
                       
                next_destination = destination[chars_i_destinations[i]]
                # Doing one action -------------------------------------------------------------------------------------
  
                if not character.has_arrived(next_destination[0], next_destination[1]):
                    print(f'Next destination {next_destination}')
                    # MOVE ONE STEP(RIGHT, LEFT, ...) TOWARDS the map position destination
                    try:
                        move_action = MoveToMapPosition(character.map_coords, next_destination)
                        character.execute_action(move_action)
                        last_action[i] = 'move'
                    except:
                        print(f'FAILED,start({character.map_coords}), destination({next_destination})')
                else:
                    # Do you know the pixel coords for this map position ? 
                    self.myPC =  self.char_pixel_coords[i][( self.char_pixel_coords[i]['x']==next_destination[0]) & ( self.char_pixel_coords[i]['y']==next_destination[1])]
                    if len(self.myPC.dropna(subset=['x'])) != 0:
                        # RECOLT ONE BLOCK OF RECOLTABLE
                        # get recoltables pixel coords of the current map position
                        next_pixel_recolt = self.myPC[['pixel_x', 'pixel_y']].values[chars_i_next_pixel_recolt[i]]
                        print('Checking/Recolting recoltables ...')
                        recolted = False
                        while not recolted and  chars_i_next_pixel_recolt[i]<len(self.myPC)-1:
                            action = Recolt(character.name, next_pixel_recolt)
                            recolted = character.execute_action(action)
                            print(f'- Trying to recolt: {next_pixel_recolt}')
                            chars_i_next_pixel_recolt[i] += 1
                            next_pixel_recolt = self.myPC[['pixel_x', 'pixel_y']].values[chars_i_next_pixel_recolt[i]]
                            time.sleep(0.3)
                            
                        last_action[i]='recolt'
                        if chars_i_next_pixel_recolt[i] == len(self.myPC)-1:
                            action = Recolt(character.name, next_pixel_recolt)
                            recolted = character.execute_action(action)
                            print(f'- Last pixel to recolt: {next_pixel_recolt}')
                            chars_i_destinations[i] += 1
                            chars_i_next_pixel_recolt[i] = 0
                        if recolted:    
                            recolt_time[i] = time.time()
                    else:
                        print('Scanning recoltables ...')
                        # SCAN ALL THE GRID FOR THE CURRENT CHARACTER - others on hold
                        scan_action = ScanMapPosition(next_destination, self.map_blueprint)
                        character.execute_action(scan_action)
                        last_action[i]='scan'
                        chars_i_destinations[i] += 1
                time.sleep(1)
        
        
    def _has_completed(self):
        for i, destinations in enumerate(self.characters_destinations_coords):
            if not self.characterObjs[i].has_arrived(destinations[-1][0], destinations[-1][1]):
                return False
        return True
    
    def _read_recoltable_coords(self):
        df = pd.read_csv(config.RECOLTABLE_MAP_BLUEPRINT_FILE_PATH)
        return df
    
    def _create_ui_handlers(self):
        # Init OCR--------------------------------
        ocrObj = OCR()
        # Init Recoltable Scanner ----------------
        recoltableScannerObj = RecoltableScanner()
        # Init monitors --------------------------
        monitors = screeninfo.get_monitors()
        monitorObjs = [MonitorWindows(i) for i, monitor in enumerate(monitors)]
        # Init UIHandlers ------------------------
        uihandlers = [UIHandler(monitorObj, ocrObj, recoltableScannerObj) for monitorObj in monitorObjs]
        return uihandlers
    
    def _init_characters(self, uihandlers):
        characterObjs = []
        for uihandler in uihandlers:
            windows = uihandler.monitor.windows
            for window in windows:
                character_name = '-'.join(window.name.split('-')[:-1]).strip()
                window.focus()
                character = Character(window.id, character_name, 100, True, uihandler)
                characterObjs.append(character)
        return characterObjs
    
    def _init_characters_destinations(self, coords: pd.DataFrame) -> list:
        # To do: filter on subscription & level
        # We suppose all the characters have the same set of destinations
        
        # Characters sorted list of destinations
        destinations = [coords[['x', 'y']].drop_duplicates().values.tolist() for _ in range(len(self.characterObjs))]
        destinations = [self.pathfinderObj.shortest_path_nearest_neighbors(character.map_coords, destinations[i]) for i, character in enumerate(self.characterObjs)]
        return destinations
   