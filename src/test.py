from monitor import Monitor 
import Quartz
import subprocess
import psutil


def main():
  MONITOR = Monitor(1,"Darwin")
  
  DOFUS_WINS = MONITOR.init_dofus_windows()
  for win in DOFUS_WINS :
    print('[x] - IS VISIBLE',win.is_visible())

  # win_number = DOFUS_WINS[0].window.get("kCGWindowNumber", 0)
  
  
  # AppleScript code to get list of window titles

  dofus_wins_pids = subprocess.check_output(['osascript', '-e', 'tell application "System Events" to get unix id of every process whose name contains "Dofus"']).decode().strip().split(', ')
  # dofus_wins_pids = dofus_wins_pids
  # output = subprocess.check_output(command_pid).decode().strip()
  # pids = output.split(", ")
  # print(dofus_wins_ids)   
  # unix_id = dofus_wins_ids

  
  
  dofus_persos = []
  for win_pid in dofus_wins_pids :
    window_name = subprocess.check_output(['osascript', '-e', f'tell application "System Events" to get name of window 1 of (every process whose unix id is {win_pid})']).decode().strip().split(' -')[0]
    dofus_persos.append(window_name)

  # build the osascript command as a list of strings
  cmd = ['osascript', '-e', 'tell application "System Events" to set frontmost of (every process whose unix id is {}) to true'.format(dofus_wins_pids[0])]

  # run the command using subprocess
  subprocess.run(cmd, check=True)
  print(dofus_persos)

  
  



  # print("[x] - FOCUS SUCCES ON WINDOW",DOFUS_WINS[0].id) if MONITOR.focus_on_window(DOFUS_WINS[0].id) == True else print("[x] - FOCUS FAILED ON WINDOW",DOFUS_WINS[0].id)

  



if __name__ == "__main__":
  main()