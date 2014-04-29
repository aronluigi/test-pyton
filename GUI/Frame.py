#!/usr/bin/python
from Tkinter import *
from p2p import kokos

class Application(Frame):
    p2p_title_label = None
    p2p_label_from = None
    p2p_input_from = None
    p2p_label_to = None
    p2p_input_to = None
    p2p_button_start = None

    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.build_frame()

    def build_frame(self):
        self.p2p_frame()

    def p2p_frame(self):
        self.p2p_title_label = Label(self, text="Scan ID range")
        self.p2p_title_label.grid()

        self.p2p_label_from = Label(self, text="From:")
        self.p2p_label_from.grid(row=1)

        self.p2p_input_from = Entry(self, width=5)
        self.p2p_input_from.grid(row=1, column=1)

        self.p2p_label_to = Label(self, text="To:")
        self.p2p_label_to.grid(row=1, column=6)

        self.p2p_input_to = Entry(self, width=5)
        self.p2p_input_to.grid(row=1, column=12)

        self.p2p_button_start = Button(self)
        self.p2p_button_start["text"] = "Start scanning"
        self.p2p_button_start["command"] = self.p2p_scan
        self.p2p_button_start.grid(row=2)

    def p2p_scan(self):
        self.p2p_button_start["text"] = str(self.p2p_input_from.get())

root = Tk()
root.title("Test Python Luigi")
root.geometry("1024x768")

app = Application(root)

root.mainloop()