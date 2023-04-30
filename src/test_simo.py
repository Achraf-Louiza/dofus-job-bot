from modules.monitor import * 
from modules.window import * 
import Quartz
import subprocess
import psutil


def main():
  print('YES')
  MONITOR = MonitorMac(1)
  
  # DOFUS_WINS = MONITOR.init_dofus_windows()
  # for win in DOFUS_WINS :
  #   print('[x] - IS VISIBLE',win.is_visible())

  # win_number = DOFUS_WINS[0].window.get("kCGWindowNumber", 0)
  
  
  # AppleScript code to get list of Dofus wndows pid and Characters names
  # dofus_wins_pids = subprocess.check_output(['osascript', '-e', 'tell application "System Events" to get unix id of every process whose name contains "Dofus"']).decode().strip().split(', ')
  
  # dofus_persos = []
  # for win_pid in dofus_wins_pids :
  #   window_name = subprocess.check_output(['osascript', '-e', f'tell application "System Events" to get name of window 1 of (every process whose unix id is {win_pid})']).decode().strip().split(' -')[0]
  #   dofus_persos.append(window_name)

  # # build the osascript command as a list of strings
  # # run the command using subprocess
  # focus_cmd_Return = subprocess.run(['osascript', '-e', 'tell application "System Events" to set frontmost of (every process whose unix id is '+dofus_wins_pids[0]+') to true'], check=True)
  # print(dofus_persos,focus_cmd_Return.returncode)

  # focus_cmd_Return = subprocess.run(['osascript', '-e', 'tell application "System Events" to set frontmost of (every process whose unix id is '+dofus_wins_pids[1]+') to true'], check=True)
  # print(dofus_persos,focus_cmd_Return.returncode)


  # print("[x] - FOCUS SUCCES ON WINDOW",DOFUS_WINS[0].id) if MONITOR.focus_on_window(DOFUS_WINS[0].id) == True else print("[x] - FOCUS FAILED ON WINDOW",DOFUS_WINS[0].id)

  



if __name__ == "__main__":
  main()