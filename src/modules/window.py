from PIL import Image
from config import *
import sys
import os
sys.path.insert(1, os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))) ; import config
import subprocess

class Window :
    """ 
      A class for the window object
    
    """

    def __init__(self, id: int, name: str  ,window  ) -> None:
      self.id = id
      self.name = name
      if (window) :
        self.window = window
        LOGS.log_build("[x] - Building Window : "+name) 
      else :
        LOGS.log_error("[x] - Failed initiating a Window")

    def focus(self) -> bool :
      pass 
    
    def is_visible(self) -> bool :
      pass

    def screenshot(self,left: int, top: int, right: int, bot: int)  -> Image :
      pass 

    def maximize(self) -> bool :
      pass



class WindowMac(Window) :
  
  def __init__(self, id: int, name: str, window) -> None:
    super().__init__(id, name, window)

  def focus(self) -> bool :
    try :
      if (OS == OS_MAC) :
        if (subprocess.run(['osascript', '-e', 'tell application "System Events" to set frontmost of (every process whose unix id is '+self.pid+') to true'], check=True).returncode != 0) :     
          return True
        else : 
          return False
    except : 
      return False
    
  def is_visible(self) -> bool :
    try :
      if (OS == 'Darwin'):
        return self.window['kCGWindowAlpha'] == '0.0'
    except :
      return False
    


    
class WindowWindows(Window) :
  def __init__(self, id: int, name: str, window) -> None:
    super().__init__(id, name, window)

  def focus(self) -> bool :
    return False
  
  def is_visible(self) -> bool :
    return False
    def __init__(self, _id: int, name: str, window):
      self.id = _id
      self.name = name
      self.window = window

    def focus(self) -> bool :
      pass
  
    def maximize(self) -> bool :
      pass

class WindowMac(Window) :
  
  def __init__(self, _id: int, name: str, window) -> None:
    super().__init__(_id, name, window)

  def focus(self) -> bool :
    try :
        return (subprocess.run(['osascript', '-e', 'tell application "System Events" to set frontmost of (every process whose unix id is '+self.pid+') to true'], check=True).returncode != 0)
    except : 
        return False

  def maximize(self) -> bool:
    script = """
      tell application "System Events"
          set frontmost of the first process whose unix id is {0} to true
          tell application "System Events" to keystroke "f" using {control down, command down}
      end tell
      """.format(self.id)
    return (subprocess.run(['osascript', '-e', script], check=True).returncode != 0)
      
  
class WindowWindows(Window) :
  def __init__(self, _id: int, name: str, window):
    super().__init__(_id, name, window)
    self.width = window.width
    self.height = window.height

  def focus(self) -> bool :
    return self.window.activate()
  
  def maximize(self) -> bool :
    return self.window.maximize()
