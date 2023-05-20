from .window import WindowWindows
import pyautogui
import pandas
from PIL import Image, ImageGrab, ImageFilter, ImageDraw
import numpy as np
import cv2 
import os, sys
import screeninfo
import time
sys.path.insert(1, os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))) ; import config

class Monitor : 
    """ 
      A class for all the windows open in a monitor
    
    """
    
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
        """
        Gets monitor top left coordinates

        """
        pass
    
    def move_cursor(self, coord_x: int, coord_y: int):
        pass
    
    def click_on_mouse(self):
        pass
    
    def focus_on_window(self, window_id: int):
        """ 
        Switches focus to the specified window identified by `window_id`.
        
        PARAMETERS
        ----------
        window_id: int
            The window id corresponding to the target window
        """
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
        pos = pyautogui.position()
        pos = [pos[0]/self.width, pos[1]/self.height]
        screenshot = self.get_box(config.P_MOUSE_LEFT + pos[0], 
                                  config.P_MOUSE_TOP + pos[1], 
                                  config.P_MOUSE_RIGHT + pos[0], 
                                  config.P_MOUSE_BOTTOM + pos[1])
        screenshot_black_box = self._extract_black_box(screenshot)
        np_array = np.array(screenshot_black_box)
        inverted_array = 255 - np_array
        return inverted_array
    
      
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
        #invert colors
        np_array = np.array(screenshot)
        inverted_array = 255 - np_array
        # Convert RGB image to grayscale
        gray_image = cv2.cvtColor(inverted_array, cv2.COLOR_RGB2GRAY)
        # Enhance the image
        enhanced = cv2.equalizeHist(gray_image)
        # Create a PIL image from the RGB array
        result_image = Image.fromarray(enhanced)
        return result_image
    
    

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

    def _extract_black_box(self, image):
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
        image = np.array(image)
        gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    
        _, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
        binary = cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernel, iterations=1)
        binary = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, kernel, iterations=3)
    
        contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
        max_area = 0
        max_contour = None
    
        for contour in contours:
            area = cv2.contourArea(contour)
            if area > max_area:
                max_area = area
                max_contour = contour
    
        if max_contour is not None:
            mask = np.zeros_like(gray)
            cv2.drawContours(mask, [max_contour], 0, (255), -1)
            black_box = cv2.bitwise_and(image, image, mask=mask)
            black_box[mask == 0] = 0
        else:
            black_box = np.array([[]])
    
        return black_box

class MonitorWindows(Monitor):
    
    def __init__(self, _id: int):
        super().__init__(_id)
        self._get_dofus_windows()
        self._get_monitor_offset()
        self.width, self.height = self.windows[0].width, self.windows[0].height
    
    def _get_dofus_windows(self):
        """
        Gets the Dofus windows associated with this monitor.
        
        """
        monitor = screeninfo.get_monitors()[self.id]
        _id = 0
        for window in pyautogui.getWindowsWithTitle('Dofus'):
            box = window.box
            if monitor.y < box.top+50 and monitor.x < box.left+50 and monitor.height > box.height-50 and monitor.width > box.width-50:
                # Check if window intersects with monitor
                my_window = WindowWindows(_id, window.title, window)
                self.windows.append(my_window)
                _id += 1
                
    def _get_monitor_offset(self):
        """
        Gets monitor top left coordinates

        """
        monitor_rect = screeninfo.get_monitors()[self.id]
        # Get the top-left corner of the monitor in pixel coordinates
        self.x_offset = monitor_rect.x 
        self.y_offset = monitor_rect.y 
    
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

