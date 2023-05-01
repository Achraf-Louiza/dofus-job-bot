from ui_handler import UIHandler
import pandas as pd
from time import time
import sys, os
sys.path.insert(1, os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))) ; import config


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
    
    
class MoveTopMapPosition(Action):
    
    def __init__(self, start: list, destination: list):
        self.start = start
        self.destination = destination
    
    def _get_direction(self) -> list:
        dx, dy = self.destination[0] - self.start[0], self.destionation[1] - self.start[1]
        direction = [abs(dx), abs(dy)].index(max(abs(dx), abs(dy)))
        monitor = self.ui_handler.monitor
        if direction==0:
            if dx==0:
                return []
            elif dx > 0:
                return config.RIGHT * monitor.width + monitor.x_offset
            else:
                return config.LEFT * monitor.width + monitor.x_offset
        else:
            if dy==0:
                return []
            elif dy > 0:
                return config.DOWN * monitor.height + monitor.y_offset
            else:
                return config.UP * monitor.height + monitor.y_offset
    
    def do(self, ui_handler: UIHandler):
        direction = self._get_direction()
        self.ui_handler.click_on_pixel(direction[0], direction[1])
        
        
class Recolt(Action):
    
    def __init__(self, recoltables:list, map_coord_x: int, map_coord_y: int):
        self.map_coord_x = map_coord_x
        self.map_coord_y = map_coord_y
        self.recoltables = recoltables
        try:
            self.df = pd.read_csv(config.RECOLTABLE_PIXEL_COORDINATES_FILE_PATH([map_coord_x, map_coord_y]))
            self.df = self.df[self.df['recoltable'].map(lambda x: x in recoltables)]
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
                        
                    