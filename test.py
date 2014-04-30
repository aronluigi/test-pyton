#!/usr/bin/python
from tkinter import *
from GUI import frame

root = Tk()
root.title("Test Python Luigi")
root.geometry("1024x768")

app = frame.Application(root)

root.mainloop()