#!/usr/bin/python
from tkinter import *
from GUI import Frame

root = Tk()
root.title("Test Python Luigi")
# root.geometry("1024x768")

app = Frame.Application(root)

root.mainloop()