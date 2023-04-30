import numpy as np
import pyautogui
from monitor import Monitor
from ocr import OCR
import config
import time
import pandas as pd

class RecoltableScanner:
    """
    A class for scanning a grid of coordinates on a monitor for specific
    text patterns using OCR.

    Attributes:
    -----------
    X : numpy.ndarray
        A 2D numpy array representing the X-coordinates of the grid.
    Y : numpy.ndarray
        A 2D numpy array representing the Y-coordinates of the grid.
    
    """     
    
    def __init__(self):
        """
        Initializes a new instance of the RecoltableScanner class.
        
        """
        self.X, self.Y = [], []
    
    def init_grid_search(self, monitor: Monitor):
        """
        Initializes the X and Y arrays based on the specified monitor dimensions.
 
        Parameters:
        -----------
        monitor : Monitor
            The monitor to use for the grid search.
            
        """
        # Define the x and y ranges
        x = range(config.P_GROUND_LEFT * monitor.width + monitor.x_offset, 
                  config.P_GROUND_RIGHT * monitor.width + monitor.x_offset, 
                  config.P_SCAN_X_SKIP)
        
        y = range(config.P_GROUND_TOP * monitor.height + monitor.y_offset, 
                  config.P_GROUND_BOTTOM * monitor.height + monitor.y_offset, 
                  config.P_SCAN_Y_SKIP)
        
        # Create the grid using meshgrid
        self.X, self.Y = np.meshgrid(x, y)
        
    
    def scan_grid(self, monitor: Monitor, ocr: OCR, recolt: bool) -> pd.DataFrame:
        """
        Scans the grid for specific text patterns using OCR and returns a DataFrame
        with the coordinates and names of the matching items.

        Parameters:
        -----------
        monitor : Monitor
            The monitor to use for the grid search.
        ocr : OCR
            The OCR object to use for text recognition.
        recolt : bool
            If True, clicks on any matching items to collect them.

        Returns:
        --------
        pd.DataFrame
            A DataFrame with the coordinates and names of the matching items.
        """
        x_coords = []
        y_coords = []
        recoltable_names = []
        for i in range(len(self.X)):
            for j in range(len(self.X[0])):
                a = i 
                b = (j if i%2==0 else len(self.X[0])- j - 1) 
                x, y = self.X[a, b], self.Y[a, b]
                monitor.move_cursor(x, y)
                time.sleep(0.3)
                black_box = monitor.get_box_near_cursor_position()
                text = ocr.recognize_text(black_box, config.ALPHABET_CHARS)
                if type(black_box) != np.ndarray:
                    black_box.close()
                for name in config.RECOLTABLE_NAMES:
                    if name in text:
                        x_coords.append(x)
                        y_coords.append(y)
                        recoltable_names.append(name)
                    if config.STR_RECOLTABLE_AVAILABLE in text or config.STR_RECOLTABLE_UNAVAILABLE not in text:
                        if recolt:
                            monitor.click_on_mouse()
                            time.sleep(3)
        df = pd.DataFrame({'name': recoltable_names, 'x': x_coords, 'y': y_coords})
        return df
        
