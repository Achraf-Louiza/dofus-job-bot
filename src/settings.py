# Move from map position to another : You can only move RIGHT, LEFT, UP, DOWN.--------------------
RIGHT = (0.81, 0.5)
LEFT = (0.18, 0.7)
DOWN = (0.4, 0.86)
UP = (0.7, 0.03)

# Map position (width or height) percentage for box edges ----------------------------------------
P_MAP_LEFT = 0.006
P_MAP_TOP = 0.065
P_MAP_RIGHT = 0.058
P_MAP_BOTTOM = 0.1

# Near current pixel coordiantes -----------------------------------------------------------------
# Percentage for box edges
P_MOUSE_LEFT = 0.005
P_MOUSE_TOP = - 0.11
P_MOUSE_RIGHT = 0.115
P_MOUSE_BOTTOM = 0.019
# Box minimal (width, height)  / Unused currently
P_MOUSE_MIN_HEIGHT = 0
P_MOUSE_MAX_HEIGHT = 0 

# Game Usable ground box cooridnates -------------------------------------------------------------
# Percentage for box edges
P_GROUND_LEFT = 0.17
P_GROUND_TOP = 0.03
P_GROUND_RIGHT = 0.83
P_GROUND_BOTTOM =0.85
# Scanner percentage of inbetween edge size in the grid search
P_SCAN_X_SKIP = 0.035
P_SCAN_Y_SKIP = 0.035