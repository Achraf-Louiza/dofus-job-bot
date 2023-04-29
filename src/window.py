




class Window :
    
    def __init__(self, name: str , window) -> None:
      self.name = name
      if (window) :
        self.window = window
        print("[x] - Initiated a Window") 
      else :
        print("[x] - Failed initiating a Window")

    def focus() -> bool :
      return False

    def screenshot(left: int, top: int, right: int, bot: int)  -> Image :
      return None 

    def maximize() -> bool :
      return None
