from monitor import Monitor 
from window import Window
from config import *
import tkinter as tk
import sys
import os






class BotApp :

  def __init__(self, os: str):

    # Start Tkinter app instance
    self.master = tk.Tk()

    # Set Tkinter app params
    self.master.geometry("900x400+300+200")
    self.master.title("DOFUS BOT V1")

    '''''
    # Create the "Close" button
    self.close_button = tk.Button(self.master, text="Close", command=self.master.destroy)
    self.close_button.grid(row=0, column=0, padx=10, pady=0)
    '''''

    # Home message
    self.home_message = "OS : " + os
    self.home_label = tk.Label(self.master, text=self.home_message)
    self.home_label.grid(row=1, column=0, padx=10, pady=10)

    # Bot messages field
    self.bot_messages = ""
    self.message_box = tk.Label(self.master, height=20, width=60, text=self.bot_messages , anchor='sw', background="#44403c")
    self.message_box.grid(row=2, column=0 ,padx=10, pady=10)
    for a in range(50):
      self.bot_messages += "\n[x] - STARTING MAC OS QUARTZ"
    self.message_box.configure(text=self.bot_messages)
    

    self.master.mainloop()
    


def main():

  
  BotApp(OS_TYPE)
  

  
  

  


if __name__ == "__main__":
  main()