import Quartz
from window import Window
from config import *
import Quartz.CoreGraphics as CG
import subprocess

class Monitor : 
    """ 
      A class for all the windows open in a monitor

      IMPORTANT NOTE : 
        The Window object returned by PyAutoGUI is a snapshot of the window at the time it was captured, 
        so you cannot directly interact with the window through the Window object.

        However, you can use the information in the Window object to manipulate the window by using other 
        libraries or system calls, such as Quartz or AppleScript. You can get the window's position and 
        size from the Window object and then use that information to move or resize the window using 
        the appropriate library or system call.
    
    """
        
    def __init__(self, id: int ) -> None:
        
        self.id = id
        LOGS.log_build("[x] - Initiating Monitor "+str(id)+ " for os "+OS)


        ## Creating windows for Mac os  
        if (OS == OS_MAC) : 
          # windows_pids = subprocess.check_output(['osascript', '-e', 'tell application "System Events" to get unix id of every process']).decode().strip().split(', ')
          self.windows = []
          '''
              In the context of CGWindowListCopyWindowInfo, the owner of a window is 
              the process that owns that window. The kCGWindowOwnerPID key provides 
              the process ID of the process that owns the window.
          '''
          windows_snapshot = Quartz.CGWindowListCopyWindowInfo(Quartz.kCGWindowListOptionAll, Quartz.kCGNullWindowID)
          for i,window in enumerate(windows_snapshot) :
            WINDOW = Window(i, window['kCGWindowOwnerName'],window)
            self.windows.append(WINDOW)
          # print([a for a in windows_filtered if ( a[0]['kCGWindowOwnerName'] == 'Dofus' and 'kCGWindowName' in a[0] and 'Dofus' in a[0]['kCGWindowName'])  ] )
        
        ## Creating windows for Wibdows
        elif (OS == OS_WINDOWS) :
          self.windows = []

        LOGS.log_build("[x] - Initiated Monitor "+str(id)+ " for os "+OS) 
        LOGS.log_build("[x] - Monitor "+str(id)+ " contain "+str(len(self.windows))+" window") 
          
    



    def get_dofus_windows(self) -> list[Window] :
      return []
    

    
