from monitor import Monitor 
from window import Window
import tkinter as tk

class BotApp :

  def __init__(self, os: str):

    # Start Tkinter app instance
    self.root = tk.Tk()

    # Set Tkinter app params
    self.root.geometry("900x400+300+200")
    self.root.title("DOFUS BOT V1")
    
    # Home message
    self.home_label = tk.Label(self.root, text="OS : " + os)
    self.home_label.grid(row=0, column=0, padx=10, pady=10)

    # Bot messages field
    self.bot_message_box = tk.Text(self.root, height=20, width=60, wrap=tk.WORD , state='disabled') # State indicates that text inside field can't be changed by user
    self.bot_message_box.grid(row=1, column=0, sticky="NSEW")
    scrollbar = tk.Scrollbar(self.root , command = self.bot_message_box.yview )
    scrollbar.grid(row=1, column=1, sticky="NS")

    self.bot_message_box.config(yscrollcommand=scrollbar.set)

    self.bot_messages = ""
    for a in range(50):
      self.bot_messages += "\n[x] - STARTING MAC OS QUARTZ"

    self.bot_message_box.configure(state='normal')            # Make text in field changeable
    self.bot_message_box.insert(tk.END, self.bot_messages)    # Change text
    self.bot_message_box.configure(state='disabled')          # Disable changing text

    # Start event listener loop
    self.root.mainloop()
    

