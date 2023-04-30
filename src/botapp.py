from monitor import Monitor 
from config import *
import tkinter as tk






class BotApp :
  """
    A class that defines the behaviour of the Tkinter app that controlls Dofus windows
    
  """

  '''NON USABLE FUNCTION. FOR TEST/DEV PURPOSES ONLY'''
  def write_random_messages_in_message_box(self):
    try :
      self.print_message_in_bot_message_box( "[x] - ", "purple")  # Private method
      self.print_message_in_bot_message_box( self.bot_messages , "green")
      for a in range(50):
        self.print_message_in_bot_message_box( "[x] - ", "purple")
        self.print_message_in_bot_message_box( "MRBO7A \n" , "green")
    except:
      LOGS.log_error("[x] - COULDNT PRINT RANDOM MESSAGES IN BOT MESSAGE BOX")
      self.root.quit()


  ''' PRIVATE METHOD '''
  def print_message_in_bot_message_box(self , message: str , color :str)->None :
    try :
      self.bot_message_box.configure(state='normal')                   # Enable text changing
      self.bot_message_box.insert(tk.END, message ,color )             # Change text
      self.bot_message_box.configure(state='disabled')                 # Disable changing text
    except :
      LOGS.log_error("[x] - COULDNT PRINT MESSAGE IN BOT MESSAGE BOX")
      self.root.quit()
  
  ''' PRIVATE METHOD '''
  def customised_bot_message_box(self):
    try :
      bot_message_box = tk.Text(self.root, height=29, width=60, wrap=tk.WORD , state='disabled') # Disable changing text
      bot_message_box.grid(row=0, column=0,  padx=10, pady=10 , sticky="NSEW")
      bot_message_box.config(highlightthickness=0) # Disable white highlighting when clicking on field

      # bot_message_box Scrollbar 
      bot_message_box_scrollbar = tk.Scrollbar(self.root , command = bot_message_box.yview )
      bot_message_box_scrollbar.grid(row=0, column=1, pady=10 , sticky="NS")
      bot_message_box.config(yscrollcommand=bot_message_box_scrollbar.set)

      # Add colors tags for text message
      bot_message_box.tag_configure("red", foreground="red")
      bot_message_box.tag_configure("green", foreground="green")
      bot_message_box.tag_configure("blue", foreground="blue")
      bot_message_box.tag_configure("white", foreground="white")
      bot_message_box.tag_configure("purple", foreground="purple")

      return bot_message_box
    except:
      self.root.quit()
      return None
    
  def select_dofus_window(self,event):
    widget = event.widget
    selection = widget.curselection()
    value = widget.get(selection[0])
    self.print_message_in_bot_message_box( "[x] - " , "purple")
    self.print_message_in_bot_message_box( "SELECTED WINDOW :"+value+"\n" , "green")
  


  def __init__(self, os: str):

    self.os = os

    # Start Tkinter app instance
    self.root = tk.Tk()

    # Set Tkinter app params
    self.root.geometry("1400x400+100+200")
    self.root.title("DOFUS BOT V1")
    
    # Home message
    self.home_label = tk.Label(self.root, text="OS : " + os )
    self.home_label.grid(row=0, column=2, padx=10, pady=10 , sticky="nw" )

    # Bot messages field
    self.bot_message_box = self.customised_bot_message_box()  # Private method

    # Printing first message in bot_message_box
    self.print_message_in_bot_message_box( "[x] - " , "purple")
    self.print_message_in_bot_message_box( "STARTING TKINTER APP\n" , "green")
    
    # Write random text in bot_message_box
    # self.write_random_messages_in_message_box()

    # Initiating a monitor
    self.monitor = Monitor(1)
    self.print_message_in_bot_message_box( "[x] - " , "purple")
    if (self.monitor):
      self.print_message_in_bot_message_box( "STARTING MONITOR 1\n" , "green")

      # Getting Dofus windows
      dofus_windows = self.monitor.get_dofus_windows()
      self.print_message_in_bot_message_box( "[x] - " , "purple")
      count_dofus_windows = len(dofus_windows)
      if (count_dofus_windows != 0) :
        self.dofus_windows_label = tk.Label(self.root, text="Windows :" )
        self.dofus_windows_label.grid(row=0, column=2, padx=10, pady=40 , sticky="nw" )
        self.print_message_in_bot_message_box( "FOUND "+str(count_dofus_windows)+" DOFUS WINDOWS\n" , "green")
        self.dofus_windows_listbox = tk.Listbox(self.root , height=count_dofus_windows , width=7 , background="#57534e")
        self.dofus_windows_listbox.grid(row=0, column=2 , pady=60 , padx=0 ,sticky="n")
        for i in range(count_dofus_windows):
            self.dofus_windows_listbox.insert(tk.END, " Dofus "+str(i+1))
        self.dofus_windows_listbox.bind("<<ListboxSelect>>", self.select_dofus_window)

    else : # Failed starting monitor
      self.print_message_in_bot_message_box( "FAILED STARTING MONITOR\n" , "green")

    # Start event listener loop
    LOGS.log_build("[x] - STARTED TKINTER APP")
    
    self.root.mainloop()



    
    

