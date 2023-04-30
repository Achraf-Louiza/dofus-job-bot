import Quartz
import sys
import os
sys.path.insert(1, os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '.'))) ; from window import Window
from config import *
import Quartz.CoreGraphics as CG
import subprocess

sys.path.insert(1, os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))) ; import config
import pyautogui
import pandas
import Quartz.CoreGraphics as CG
from PIL import Image, ImageGrab
import numpy as np
import cv2 

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
    

    
    
    
        
    def __init__(self, _id: int):
        self.id = _id
        # Attributes that need to be defined in subsclasses
        self.windows = []
        self.y_offset = 0
        self.x_offset = 0
        
    def _get_dofus_windows(self):
        """
        Gets the Dofus windows associated with this monitor.
        """
        pass
    
    def _get_monitor_offset(self):
        pass
    
    def focus_on_window(self, window_id: int):
        self.windows[window_id].focus()
    
    def get_box(self, p_left: float, p_top: float, p_right: float, p_bottom: float) -> Image:
        """
        Screenshots the box defined by the coordinates and return an Image

        Parameters
        ----------
        p_left : float
            Percentage of width for left x pixel coordinate
        p_top : float
            Percentage of height for top y pixel coordinate
        p_right : float
            Percentage of width for right x pixel coordinate
        p_bottom : float
            Percentage of height for bottom y pixel coordinate

        Returns
        -------
        Image
            Image of the box's screenshot

        """
        # Define the region of the screen to capture as a percentage of the screen size
        left = int(self.width * p_left) + self.x_offset
        top = int(self.height * p_top) + self.y_offset
        right = int(self.width * p_right) + self.x_offset
        bottom = int(self.height * p_bottom) + self.y_offset
        # Define bbox
        bbox = (left, top, right, bottom)
        # Take a screenshot of the defined region
        img = ImageGrab.grab(bbox)
        return img
    
    def get_box_near_cursor_position(self) -> Image:
        """
        Gets a screenshot of a box near cursor position [box relative coordinates are in config.py]
    
        Returns
        -------
        Image
            Screenshot of the black box near cursor position or empty image array([[]]) if none are detected
    
        """
        screenshot = self.get_box(config.P_MOUSE_LEFT, 
                                  config.P_MOUSE_TOP, 
                                  config.P_MOUSE_RIGHT, 
                                  config.P_MOUSE_BOTTOM)
        screenshot_black_box = self._extract_black_box(screenshot)
        return screenshot_black_box
    
      
    def get_box_map_position(self) -> Image:
        """
        Gets a screenshot of a box around map position [box relative coordinates are in config.py]

        Returns
        -------
        Image
            Screenshot of the box around map position

        """
        screenshot = self.get_box(config.P_MAP_LEFT, 
                                  config.P_MAP_TOP, 
                                  config.P_MAP_RIGHT, 
                                  config.P_MAP_BOTTOM)
        return screenshot
    
    def get_clickable_game_zone(self) -> Image:
        """
        Gets a screenshot of the usable ground in the game [box relative coordiantes are in config.py]

        Returns
        -------
        Image
            Screenshot of the box including usable ground in the game

        """
        screenshot = self.get_box(config.P_GROUND_LEFT, 
                                  config.P_GROUND_TOP, 
                                  config.P_GROUND_RIGHT, 
                                  config.P_GROUND_BOTTOM)
        return screenshot
    
    def _extract_black_box(self, image: Image) -> Image:
        """
        Exctracts the most prominent black box in the image

        Parameters
        ----------
        image : Image
            An Image where a black box should be included

        Returns
        -------
        Image
            Image f the black box inside the input image

        """
        # Convert the PIL image to a numpy array
        image = np.array(image)
        #plt.imshow(image)
        # Convert the numpy array to a cv2 image
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        # Convert the image to grayscale
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        # Define the lower and upper boundaries of the black color
        lower = np.array([0, 0, 0], dtype=np.uint8)
        upper = np.array([30, 30, 30], dtype=np.uint8)
        # Create a mask of the black pixels
        mask = cv2.inRange(image, lower, upper)
        # Find the contours of the black box
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        try:
            # Find the bounding box of the black box
            x, y, w, h = cv2.boundingRect(contours[0])
            # Extract the black box from the original image using the bounding box
            black_box = image[y:y+h, x:x+w]
        except:
            black_box=np.array([[]])
        return black_box
        

class MonitorMac(Monitor):
    
    def __init__(self, _id: int):
        super().__init__(_id)
        self._get_dofus_windows()
        self._get_monitor_offset()
        
    def _get_dofus_windows(self):        
        windows_snapshot = Quartz.CGWindowListCopyWindowInfo(Quartz.kCGWindowListOptionAll, Quartz.kCGNullWindowID)
        for i, window in enumerate(windows_snapshot) :
            my_window = Window(i, window['kCGWindowOwnerName'],window)
            self.windows.append(my_window)
    
    def _get_monitor_offset():
        pass
    
    
class MonitorWindows(Monitor):
    
    def __init__(self, _id: int):
        super().__init__(_id)
        self._get_dofus_windows()
        self._get_monitor_offset
        
    def _get_dofus_windows(self):
        monitor_rect = pyautogui.locateOnScreen(self._id)
        _id = 0
        for window in pyautogui.getWindowsWithTitle('Dofus'):
            if pyautogui.getWindowRect(window)[0] < monitor_rect[2] and pyautogui.getWindowRect(window)[1] < monitor_rect[3] and pyautogui.getWindowRect(window)[2] > monitor_rect[0] and pyautogui.getWindowRect(window)[3] > monitor_rect[1]:
                # Check if window intersects with monitor
                my_window = Window(_id, window.title, window)
                self.windows.append(my_window)
                _id += 1
                
    def _get_monitor_offset(self):
        monitor_rect = pyautogui.getMonitors()[self._id]
        # Get the top-left corner of the monitor in pixel coordinates
        self.x_offset = monitor_rect.left 
        self.y_offset = monitor_rect.top 
    
    def move_cursor(self, coord_x: int, coord_y: int):
        """
        Moves the cursor to the specified coordinates.
 
        Args:
            coord_x (int): The x-coordinate of the destination.
            coord_y (int): The y-coordinate of the destination.
        """
        x = coord_x + self.x_offset
        y = coord_y + self.y_offset
        pyautogui.moveTo((x, y))
    
    def click_on_mouse(self):
        """
        Simulates a left-click on the mouse at the current cursor position.
        """
        pyautogui.click(button='left')
