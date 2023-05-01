from action import Action
from ui_handler import UIHandler
import numpy as np

class Character:
    
    def __init__(self, _id: int, name: str, level: int, is_subscribed: bool, ui_handler: UIHandler) -> None:
        self.id = _id
        self.name = name
        self.level = level
        self.is_subscribed = is_subscribed
        self.ui_handler = ui_handler
        self.map_coords = ui_handler.extract_current_map_position(_id)


    def execute_action(self, action : Action) -> bool :
        return action.do()
    
    def execute_strategy(self, strategy: list) -> bool :
        c = 0
        executed = True
        while (c<len(strategy) and executed ):
            executed = self.execute_action(strategy[c])!=False
            c+=1
        return executed 
        
    def has_moved(self, new_map_coords: list):
        return self.map_coords[0] != new_map_coords[0] or self.map_coords[1] != new_map_coords[1]
    
    def update_map_coords(self, new_map_coords: list):
        self.map_coords = new_map_coords

    def has_arrived(self, pos_x: int, pos_y: int) -> bool:
        return self.map_coords[0]==pos_x and self.map_coords[1]==pos_y
        
    def read_current_position(self):
        return self.ui_handler.extract_current_map_position(self.id)