import Quartz
from window import Window
from config import *
import Quartz.CoreGraphics as CG
import subprocess

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
          dofus_wins_pids = subprocess.check_output(['osascript', '-e', 'tell application "System Events" to get unix id of every process whose name contains "Dofus"']).decode().strip().split(', ')
          self.windows = []
          # for pid in dofus_wins_pids : 
          #   self.windows.append()
          
          
          
        
        ## WINDOWS
        elif (os == "windows") :
          self.windows = []

        LOGS.log_build("[x] - Initiated Monitor "+str(id)+ " for os "+os) 
        LOGS.log_build("[x] - Monitor "+str(id)+ " contain "+str(len(self.windows))+" window") 
          
    

    def init_dofus_windows(self) -> list[Window] :
      return []
    

    
