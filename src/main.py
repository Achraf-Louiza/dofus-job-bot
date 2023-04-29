from botapp import BotApp
from config import *


'''

  Start Tkinter app based on command line param or the os version stored in OS_TYPE
      - python main.py                  ---> WILL RUN TKINTER APP DEPENDING ON SYSTEM OS
      - python main.py macos            ---> WILL RUN TKINTER APP DEPENDING ON MAC OS
      - python main.py windows          ---> WILL RUN TKINTER APP DEPENDING ON WINDOWS OS

'''
def main():
  if (argv[1]) :
    BotApp(argv[1])
  else :
    BotApp(OS_TYPE)
  
if __name__ == "__main__":
  main()


