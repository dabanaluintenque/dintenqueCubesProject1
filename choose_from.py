# author: Dabana Intenque
from tkinter import Tk


second_window = Tk()
second_window.title("Choose to update or to visualize data")
second_window.geometry("500x200+200+500")


def runSecondWindow():
    second_window.mainloop()


if __name__ == '__main__':
    runSecondWindow()
