import Quartz
from window import Window


class Monitor : 
    def __init__(self, id: int , os:str) -> None:
        self.id = id
        self.os = os
        if (os == "macos") : 
          self.windows = Quartz.CGWindowListCopyWindowInfo(Quartz.kCGWindowListExcludeDesktopElements , Quartz.kCGNullWindowID)
        elif (os == "windows") :
          self.windows = None
    def get_dofus_windows() -> list(Window)
      windows_dofus_list = []
      for window in self.windows :
          if window[Quartz.kCGWindowOwnerName] == "Dofus" :
              windows_dofus_list.append(Window("Dofus",window)) 
      return windows_dofus_list