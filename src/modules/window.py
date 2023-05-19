from PIL import Image
import sys
import os
import pyautogui
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
  
class WindowWindows(Window) :
  def __init__(self, _id: int, name: str, window):
    super().__init__(_id, name, window)
    self.width = window.width
    self.height = window.height

  def focus(self) -> bool :
      try:
          self.window.activate()
      except:
          self.window.minimize()
          self.window.maximize()
          
  def maximize(self) -> bool :
    return self.window.maximize()
