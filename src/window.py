from PIL import Image





class Window :
    """ 
      A class for the window object
    
    """
    
    def __init__(self, name: str , window) -> None:
      self.name = name
      if (window) :
        self.window = window
        print("[x] - Initiated a Window") 
      else :
        print("[x] - Failed initiating a Window")

    def focus(self) -> bool :
      return False

    def screenshot(self,left: int, top: int, right: int, bot: int)  -> Image :
      return None 

    def maximize(self) -> bool :
      return False
