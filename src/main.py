from botapp import BotApp
from config import *
import sys


'''

  Start Tkinter app based on command line param or the os version stored in OS
      - python main.py                  ---> WILL RUN TKINTER APP DEPENDING ON SYSTEM OS
      - python main.py macos            ---> WILL RUN TKINTER APP DEPENDING ON MAC OS
      - python main.py windows          ---> WILL RUN TKINTER APP DEPENDING ON WINDOWS OS

'''
def main(os):
  if (os) :
    BotApp(os[0])
  else :
    BotApp(OS)

  LOGS.log_build("[x] - Quitted Tkinter app")

  
if __name__ == "__main__":
  main(sys.argv[1:])


