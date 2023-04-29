from monitor import Monitor 
from window import Window
import tkinter as tk
import sys
import os




class BotApp :

  def __init__(self):
    self.master = tk.Tk()
    self.master.geometry("900x400+300+200")
    self.master.title("DOFUS BOT V1")

    self.home_message = "Select an os :"
    self.app_messages = "[x] - SELECTED OS : Mac OS"

    '''''
    # Create the "Close" button
    self.close_button = tk.Button(self.master, text="Close", command=self.master.destroy)
    self.close_button.grid(row=0, column=0, padx=10, pady=0)
    '''''

    # Home message
    self.home_label = tk.Label(self.master, text=self.home_message)
    self.home_label.grid(row=1, column=0, padx=10, pady=10)


    # Create the OS choice buttons
    self.macos_button = tk.Button(self.master, text="Mac OS", command=self.start_mac_os_monitor)
    self.macos_button.grid(row=2, column=0, padx=40, pady=10)
    self.windows_button = tk.Button(self.master, text="Windows", command=self.start_windows_monitor)
    self.windows_button.grid(row=2, column=2, padx=0, pady=10)

    self.master.mainloop()

  def start_mac_os_monitor(self)->None:
    print("[x] - APP STARTING MAC OS MONITOR")
    self.home_label.configure(text = "OS X")
    self.home_label.grid(row=1, column=0, padx=10, pady=10)
    self.windows_button.destroy()
    self.macos_button.destroy()
    msg_box = self.place_field_text()
    for a in range(50):
      self.app_messages += "\n[x] - STARTING MAC OS QUARTZ"
    msg_box.configure(text=self.app_messages)

  def start_windows_monitor(self) -> None :
    print("[x] - APP STARTING WINDOWS MONITOR")

  def place_field_text(self):
    self.message_box = tk.Label(self.master, height=20, width=60, text=self.app_messages , anchor='sw', background="#44403c")
    self.message_box.grid(row=2, column=0 ,padx=10, pady=10)
    return self.message_box


    



def main():

  
  
  BotApp()
  

  
  

  


if __name__ == "__main__":
  main()