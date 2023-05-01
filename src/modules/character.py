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
    
    def has_moved(self):
        new_map_coords = self.ui_handler.extract_current_map_position(self.id)
        if self.map_coords[0] != new_map_coords[0] or self.map_coords[1] != new_map_coords[1]:
            return True
        return False
       
    
'''


def click_on(target):
    x1, y1 = pyautogui.position()
    x2, y2 = target
    # calculate the distance between the two points
    dx = x2 - x1
    dy = y2 - y1
    distance = (dx ** 2 + dy ** 2) ** 0.5
    
    # set the number of steps to take between the two points
    num_steps = 3
    
    # loop over the number of steps and move the cursor gradually
    for step in range(num_steps):
        # calculate the current position based on the step number
        x = int(x1 + step * dx / num_steps)
        y = int(y1 + step * dy / num_steps)
    
        # add some random noise to the position
        x += random.randint(-5, 5)
        y += random.randint(-5, 5)
    
        # move the cursor to the current position
        pyautogui.moveTo(x, y)
    
        # add a random delay between 0.1 and 0.3 seconds
        time.sleep(random.uniform(1e-8, 3e-8))
        
    # move the cursor to the final position
    pyautogui.moveTo(x2, y2)



def where_am_I(pos, action):
    if action == RIGHT:
        pos[0] += 1
    elif action == LEFT:
        pos[0] -= 1
    elif action == UP:
        pos[1] -=1
    elif action == DOWN:
        pos[1] +=1
    return pos
  
def wait_human_like():
    coords = pyautogui.position()
    for _ in range(np.random.randint(2, 4)):
        move_to((np.random.uniform((coords[0]+np.random.uniform(-300, 300), coords[1]+np.random.uniform(-180, 180)))))
        time.sleep(abs(np.random.normal(1.5, 0.5)))
'''