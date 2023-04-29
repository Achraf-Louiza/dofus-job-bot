from monitor import Monitor 
from window import Window
import tkinter as tk






class BotApp :

  '''NON USABLE FUNCTION FOR TEST/DEV PURPOSES ONLY'''
  def write_random_messages_in_message_box(self):
    self.print_message_in_bot_message_box( "[x] - ", "purple")  # Private method
    self.print_message_in_bot_message_box( self.bot_messages , "green")
    for a in range(50):
      self.print_message_in_bot_message_box( "[x] - ", "purple")
      self.print_message_in_bot_message_box( "MRBO7A \n" , "green")


  ''' PRIVATE METHOD '''
  def print_message_in_bot_message_box(self , message: str , color :str)->None :
      self.bot_message_box.configure(state='normal')                   # Make text in field changeable
      self.bot_message_box.insert(tk.END, message ,color )             # Change text
      self.bot_message_box.configure(state='disabled')                 # Disable changing text
  
  ''' PRIVATE METHOD '''
  def customised_bot_message_box(self):
    bot_message_box = tk.Text(self.root, height=26, width=60, wrap=tk.WORD , state='disabled') # State indicates that text inside field can't be changed by user
    bot_message_box.grid(row=1, column=0,  padx=10, pady=10 , sticky="NSEW")
    bot_message_box.config(highlightthickness=0) # Disable white highlighting when clicking on field

    # bot_message_box Scrollbar 
    bot_message_box_scrollbar = tk.Scrollbar(self.root , command = bot_message_box.yview )
    bot_message_box_scrollbar.grid(row=1, column=1, pady=10 , sticky="NS")
    bot_message_box.config(yscrollcommand=bot_message_box_scrollbar.set)

    # Add colors tags for text message
    bot_message_box.tag_configure("red", foreground="red")
    bot_message_box.tag_configure("green", foreground="green")
    bot_message_box.tag_configure("blue", foreground="blue")
    bot_message_box.tag_configure("white", foreground="white")
    bot_message_box.tag_configure("purple", foreground="purple")

    return bot_message_box
  


  def __init__(self, os: str):

    # Start Tkinter app instance
    self.root = tk.Tk()

    # Set Tkinter app params
    self.root.geometry("900x400+300+200")
    self.root.title("DOFUS BOT V1")
    
    # Home message
    self.home_label = tk.Label(self.root, text="OS : " + os )
    self.home_label.grid(row=0, column=0, padx=10, pady=10 , sticky="w" )

    # Bot message
    self.bot_messages = "STARTING TKINTER APP\n"

    # Bot messages field
    self.bot_message_box = self.customised_bot_message_box()  # Private method
    
    # Write random text in bot_message_box
    self.write_random_messages_in_message_box()

    # Start event listener loop
    self.root.mainloop()



    
    

