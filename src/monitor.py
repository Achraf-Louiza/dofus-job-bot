import Quartz
from window import Window
from config import *
import objc
from AppKit import NSWorkspace, NSWindow

class Monitor : 
    """ 
      A class for all the windows open in a monitor
    
    """
        
    def __init__(self, id: int , os:str) -> None:
        
        self.id = id
        self.os = os
        LOGS.log_build("[x] - Initiating Monitor "+str(id)+ " for os "+os)


        ## MACOS  
        if (os == "Darwin") : 
          windows = []
          # for app in NSWorkspace.sharedWorkspace().launchedApplications():
              # app_windows = app['NSApplicationWindows']
              # if app_windows:
              # windows += app
          self.windows = []
          # visible_windows = filter(lambda w: w.isVisible(), windows)
          windows = Quartz.CGWindowListCopyWindowInfo(Quartz.kCGWindowListOptionOnScreenOnly , Quartz.kCGNullWindowID)
          window_id = 1
          for window in windows : 
            if 'kCGWindowOwnerName' in window:
              self.windows.append(Window(window['kCGWindowOwnerName'],window_id,window))
              window_id+=1
          
          
          
        
        ## WINDOWS
        elif (os == "windows") :
          self.windows = []

        LOGS.log_build("[x] - Initiated Monitor "+str(id)+ " for os "+os) 
        LOGS.log_build("[x] - Monitor "+str(id)+ " contain "+str(len(self.windows))+" window") 
          
    

    def get_dofus_windows(self) -> list[Window] :
      dofus_windows_list = []
      for window in self.windows :
          if window.name == "Dofus" :
              dofus_windows_list.append(window)
      LOGS.log_build("[x] - Found "+str(len(dofus_windows_list))+" Dofus windows")
      return dofus_windows_list

    
