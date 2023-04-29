import Quartz
from window import Window


class Monitor : 
    """ 
      A class for all the windows open in a monitor
    
    """
        
    def __init__(self, id: int , os:str) -> None:
        
        self.id = id
        self.os = os

        ## MACOS  
        if (os == "macos") : 
          self.windows = Quartz.CGWindowListCopyWindowInfo(Quartz.kCGWindowListExcludeDesktopElements , Quartz.kCGNullWindowID)
        
        ## WINDOWS
        elif (os == "windows") :
          self.windows = []

        if (self.windows == None) :
          self.windows = []
          
    

    def get_dofus_windows(self) -> list[Window] :
      
      windows_dofus_list = []

      ## MACOS  
      if (self.os == "macos") :
        for window in self.windows :
            if window[Quartz.kCGWindowOwnerName] == "Dofus" :
                windows_dofus_list.append(Window("Dofus",window))


      ## WINDOWS 
      elif (self.os == "windows") :
         print("WINDOWS..")
        
      print("[x] - GETTING DOFUS WINDOWS : FOUND "+ str(len(windows_dofus_list))+" DOFUS WINDOWS")
      return windows_dofus_list