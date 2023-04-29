from botapp import BotApp
from config import *


'''
  Start Tkinter app depending on the os version stored in OS_TYPE
'''

  
def main():
  BotApp(OS_TYPE)
  
if __name__ == "__main__":
  main()


