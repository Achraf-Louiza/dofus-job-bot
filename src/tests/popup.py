from tkinter import *

#Create an instance of Tkinter frame
win = Tk()
win.geometry("350x100")  
popup_opened = False

def open_popup_test_finished():
    global popup_opened
    if not popup_opened:
        top = Toplevel()
        top.geometry("350x80")
        top.title("Test execution notifier")
        Label(top, text="All the tests have been executed", font=('bold')).place(x=10,y=10)
        popup_opened = True
        win.mainloop()