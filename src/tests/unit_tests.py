from uihandler_testor import TestUIHandler

def main():
    # UIHandler test
    uihandler_testor = TestUIHandler()
    uihandler_testor.test_screenshot_map_position_img()
    """uihandler_testor.test_extract_map_position()
    uihandler_testor.test_screenshot_near_cursor_img()
    uihandler_testor.test_ocr()"""
    #uihandler_testor.test_scan_map_recoltables()
    #uihandler_testor.test_basic_movement_coords()
    uihandler_testor.test_screenshot_near_cursor_img()
    uihandler_testor.test_ocr()
    

# Run main
main()