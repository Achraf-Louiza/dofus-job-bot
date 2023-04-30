from PIL import Image
from config import *





class Window :
    """ 
      A class for the window object
    
    """
    
    def __init__(self, name: str , id: int ,window , os:str) -> None:
      self.os = os
      self.id = id
      self.name = name
      if (window) :
        self.window = window
        LOGS.log_build("[x] - Building Window : "+name) 
      else :
        LOGS.log_error("[x] - Failed initiating a Window")

    def focus(self) -> bool :
      try :
        return True
      except :
        return False
      
    def is_visible(self) -> bool :
      try :
        if (self.os == 'Darwin'):
          return self.window['kCGWindowAlpha'] == '0.0'

      except Exception as e :
        print(e)
        return 

    def screenshot(self,left: int, top: int, right: int, bot: int)  -> Image :
      return None 

    def maximize(self) -> bool :
      return False
