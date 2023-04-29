import pyautogui as pag
import pygetwindow as pgw
import Quartz


class Windows : 
    def __init__(self):
        self.windows = Quartz.CGWindowListCopyWindowInfo(Quartz.kCGWindowListExcludeDesktopElements , Quartz.kCGNullWindowID)
    def get_win(self,name):
        for window in self.windows :
            if window[Quartz.kCGWindowOwnerName] == name :
                return window
        return None 



class Dofus_Win :
    def __init__(self) :
        self.win = Windows().get_win("Dofus")
        if (self.win is not None):
            print("[X] - Dofus Window found.")
        else :
            print('[x] - Dofus window not found.')
            
    def get_win(self) :
        return self.win

    def start_bot(self) :
        if (win is None):
            print("[x] -- FAILED STARTING BOT")
        else :
            print("[X] -- STARTING BOT :")



def main():
    dofus_win = Dofus_Win()


if __name__ == "__main__":
    main()
