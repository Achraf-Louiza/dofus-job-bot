class Window :
    """ 
      A class for the window object
    
    """
    def __init__(self, _id: int, name: str, window):
      self.id = _id
      self.name = name
      self.width = window.width
      self.height = window.height
      self.window = window

    def focus(self) -> bool :
        try:
            self.window.activate()
        except:
            self.window.minimize()
            self.window.maximize()
              
    def maximize(self) -> bool :
      return self.window.maximize()
  
   


