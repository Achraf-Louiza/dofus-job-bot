from monitor import Monitor 
from window import Window
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

    # Home message
    self.home_label = tk.Label(self.master, text="OS : " + os).grid(row=1, column=0, padx=10, pady=10)

    # Bot messages field
    self.bot_messages = ""
    self.bot_message_box = tk.Label(self.master, height=20, width=60, text=self.bot_messages , anchor='sw', background="#44403c")
    self.bot_message_box.grid(row=2, column=0 ,padx=10, pady=10)
    for a in range(50):
      self.bot_messages += "\n[x] - STARTING MAC OS QUARTZ"
    self.bot_message_box.configure(text=self.bot_messages)
    

    self.master.mainloop()
    

