import numpy as np
import pyautogui
from .monitor import Monitor
from .ocr import OCR
import time
import pandas as pd
import sys, os
from unidecode import unidecode
sys.path.insert(1, os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))) ; import config

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
        x = range(int((config.P_GROUND_LEFT+0.01) * monitor.width + monitor.x_offset), 
                  int((config.P_GROUND_RIGHT+0.01) * monitor.width + monitor.x_offset), 
                  int(config.P_SCAN_X_SKIP*monitor.width))
        
        y = range(int((config.P_GROUND_TOP+0.04) * monitor.height + monitor.y_offset), 
                  int((config.P_GROUND_BOTTOM-0.025) * monitor.height + monitor.y_offset), 
                  int(config.P_SCAN_Y_SKIP*monitor.height))
        
        # Create the grid using meshgrid
        self.X, self.Y = np.meshgrid(x, y)
        
    
    def scan_grid(self, map_pos: list, monitor: Monitor, ocr: OCR, recolt: bool) -> pd.DataFrame:
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
                time.sleep(0.35)
                black_box = monitor.get_box_near_cursor_position()
                if black_box.shape[0]<40 or black_box.shape[1]<10:
                    text = ''
                else:
                    text = ocr.recognize_text(black_box, config.ALPHABET_CHARS)
                    text = unidecode(text.lower())
                    print('-------------------------------------------')
                    print(text)
                for name in config.RECOLTABLE_NAMES:
                    # Clean text
                    if name in text:
                        x_coords.append(x)
                        y_coords.append(y)
                        recoltable_names.append(config.mapToRecoltable[name])
                        print(name, x, y)
                        if recolt and (config.STR_RECOLTABLE_AVAILABLE in text and config.STR_RECOLTABLE_UNAVAILABLE not in text):
                            print(f'HERE {recolt}')
                            if name =='ble' or name == 'bl\n' or name=='orge' or name=='seigle':
                                monitor.click_on_mouse()
                                time.sleep(2)
            if type(black_box) != np.ndarray:
                black_box.close()
            
        df = pd.DataFrame({'recoltable': recoltable_names, 'x': [map_pos[0]]*len(x_coords), 'y': [map_pos[1]]*len(x_coords), 'pixel_x': x_coords, 'pixel_y': y_coords})
        try:
            origin = pd.read_csv(config.RECOLTABLE_PIXEL_COORDINATES)
        except:
            origin = pd.DataFrame()
        df = pd.concat([origin, df], ignore_index=True)
        df = df.drop_duplicates()
        df.to_csv(config.RECOLTABLE_PIXEL_COORDINATES, index=False)
        return df
        
