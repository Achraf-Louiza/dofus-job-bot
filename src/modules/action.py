from .ui_handler import UIHandler
import pandas as pd
import time
import sys, os
sys.path.insert(1, os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))) ; import settings, config;


class Action :
    
    def __init__(self):
        pass

    def do(self, ui_hanlder: UIHandler)-> bool :
        pass

class ClickOnCoords(Action) : 

    def __init__(self, coord_x: int, coord_y: int)->None :
        super().__init__()
        self.coord_x = coord_x
        self.coord_y = coord_y

    def do(self, ui_handler: UIHandler) -> bool :
        return ui_handler.click_on_pixel(self.coord_x, self.coord_y)
    
    
class MoveToMapPosition(Action):
    
    def __init__(self, start: list, destination: list):
        self.start = start
        self.destination = destination
    
    def _get_direction(self, ui_handler) -> list:
        dx, dy = self.destination[0] - self.start[0], self.destination[1] - self.start[1]
        direction = [abs(dx), abs(dy)].index(max(abs(dx), abs(dy)))
        monitor = ui_handler.monitor
        if direction==0:
            if dx==0:
                return []
            elif dx > 0:
                return (settings.RIGHT[0] * monitor.width, settings.RIGHT[1]*monitor.height)
            else:
                return (settings.LEFT[0] * monitor.width, settings.LEFT[1]*monitor.height)
        else:
            if dy==0:
                return []
            elif dy > 0:
                return (settings.DOWN[0] * monitor.width, settings.DOWN[1]*monitor.height) 
            else:
                return (settings.UP[0] * monitor.width, settings.UP[1]*monitor.height) 
    
    def do(self, ui_handler: UIHandler):
        direction = self._get_direction(ui_handler)
        ui_handler.click_on_pixel(direction[0], direction[1])
        

class Recolt(Action):
    
    def __init__(self, character_name, pixel_coords):
        self.pixel_coord_x, self.pixel_coord_y = pixel_coords
        self.character_name = character_name
  
               
    def do(self, ui_handler: UIHandler):
        ui_handler.monitor.move_cursor(self.pixel_coord_x, self.pixel_coord_y)
        text_near_mouse = ui_handler.extract_text_near_cursor()
        recoltables = config.recoltablesPerChar[self.character_name]
        for recoltable in recoltables:
            if recoltable in text_near_mouse:
                if (config.STR_RECOLTABLE_AVAILABLE in text_near_mouse or config.STR_RECOLTABLE_UNAVAILABLE not in text_near_mouse):
                    ui_handler.monitor.click_on_mouse()
                    return 1
        """except:
            print(f'Error extracting text near cusor {self.pixel_coord_x}, {self.pixel_coord_y}')"""
        
        return 0

class ScanMapPosition(Action):
    
    def __init__(self, map_pos, blueprint):
        self.map_pos = map_pos
        self.map_coord_x,  self.map_coord_y = map_pos
        self.blueprint = blueprint

    def do(self, ui_handler: UIHandler):
        ui_handler.scan_map_recoltables(self.map_pos, recolt=True)
                            
class Recolt_all(Action):
    
    def __init__(self, recoltables:list, map_coord_x: int, map_coord_y: int):
        self.map_coord_x = map_coord_x
        self.map_coord_y = map_coord_y
        self.recoltables = recoltables
        try:
            self.df = pd.read_csv(config.RECOLTABLE_PIXEL_COORDINATES_FILE_PATH([map_coord_x, map_coord_y]))
            #self.df = self.df[self.df['recoltable'].map(lambda x: x in recoltables)]
        except:
            self.df = pd.DataFrame()
    
    def do(self, ui_handler: UIHandler):
        if len(self.df) == 0:
            df = ui_handler.scan_map_recoltables(recolt=True)
            df.to_csv(config.RECOLTABLE_PIXEL_COORDINATES_FILE_PATH([self.map_coord_x, self.map_coord_y]))
        else:
            for i, row in self.df.iterrows():
                ui_handler.monitor.move_cursor(row.x, row.y)
                time.sleep(0.5)
                text_near_mouse = ui_handler.extract_text_near_cursor()
                if row.recoltable in text_near_mouse:
                    if config.STR_RECOLTABLE_AVAILABLE in text_near_mouse or config.STR_RECOLTABLE_UNAVAILABLE not in text_near_mouse:
                        ui_handler.monitor.click_on_mouse()
                        time.sleep(3)

                    