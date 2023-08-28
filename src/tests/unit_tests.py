from uihandler_testor import TestUIHandler
from PIL import Image
import numpy as np

def main():
    # UIHandler test
    uihandler_testor = TestUIHandler()
    uihandler_testor.test_screenshot_map_position_img()
    """img1 = np.array(Image.open("../../data/images/infight_reference.png"))
    img2 = np.array(uihandler_testor.test_screenshot_infight_img())
    measure = uihandler_testor.measure(img1, img2)
    print('MEASURE GIVES: ', measure)"""
    uihandler_testor.test_extract_map_position()
    """uihandler_testor.test_screenshot_near_cursor_img()
    uihandler_testor.test_ocr()"""
    #uihandler_testor.test_scan_map_recoltables()
    #uihandler_testor.test_basic_movement_coords()
    #uihandler_testor.test_screenshot_near_cursor_img()
    uihandler_testor.test_ocr()
    #uihandler_testor.test_surrender_button_pos()
    

# Run main
main()