from monitor import Monitor 
from window import Window
import tkinter as tk

class BotApp :

  def print_message_in_bot_message_box(self , message: str , color :str)->None :
      self.bot_message_box.configure(state='normal')                   # Make text in field changeable
      self.bot_message_box.insert(tk.END, message ,color )             # Change text
      self.bot_message_box.configure(state='disabled')                 # Disable changing text

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
    self.bot_message_box = tk.Text(self.root, height=26, width=60, wrap=tk.WORD , state='disabled') # State indicates that text inside field can't be changed by user
    self.bot_message_box.grid(row=1, column=0,  padx=10, pady=10 , sticky="NSEW")
    self.bot_message_box.config(highlightthickness=0) # Disable white highlighting when clicking on field

    # bot_message_box Scrollbar 
    self.bot_message_box_scrollbar = tk.Scrollbar(self.root , command = self.bot_message_box.yview )
    self.bot_message_box_scrollbar.grid(row=1, column=1, pady=10 , sticky="NS")
    self.bot_message_box.config(yscrollcommand=self.bot_message_box_scrollbar.set)

    self.bot_messages = "STARTING TKINTER APP\n"
    # for a in range(50):
    #   self.bot_messages += "\n[x] - STARTING MAC OS QUARTZ"

    self.bot_message_box.tag_configure("red", foreground="red")
    self.bot_message_box.tag_configure("green", foreground="green")
    self.bot_message_box.tag_configure("blue", foreground="blue")
    self.bot_message_box.tag_configure("white", foreground="white")
    self.bot_message_box.tag_configure("purple", foreground="purple")
    
    self.print_message_in_bot_message_box( "[x] - ", "purple")
    self.print_message_in_bot_message_box( self.bot_messages , "green")
    for a in range(50):
      self.print_message_in_bot_message_box( "[x] - ", "purple")
      self.print_message_in_bot_message_box( "MRBO7A \n" , "green")

    # Start event listener loop
    self.root.mainloop()



    
    

