from PIL import Image
import sys
import os
sys.path.insert(1, os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))) ; import config
import subprocess

class Window :
    """ 
      A class for the window object
    
    """
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
