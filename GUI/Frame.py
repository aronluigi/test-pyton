#!/usr/bin/python
from tkinter import *
from p2p import kokos


class Application(Frame):
    p2p_title_label = None
    p2p_label_from = None
    p2p_input_from = None
    p2p_label_to = None
    p2p_input_to = None
    p2p_label_alert = None
    p2p_button_start = None

    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.build_frame()

    def build_frame(self):
        self.p2p_frame()

    def p2p_frame(self):
        self.p2p_title_label = Label(self, text="Scan ID range", width=50, anchor=W)
        self.p2p_title_label.grid(row=0, column=0, columnspan=4, sticky=W)

        self.p2p_label_from = Label(self, text="From:")
        self.p2p_label_from.grid(row=1, column=0, sticky=W)

        self.p2p_input_from = Entry(self, width=10)
        self.p2p_input_from.insert(0, "8488")
        self.p2p_input_from.grid(row=1, column=1, sticky=W)

        self.p2p_label_to = Label(self, text="To:")
        self.p2p_label_to.grid(row=1, column=2, sticky=W)

        self.p2p_input_to = Entry(self, width=10, text="0")
        self.p2p_input_to.insert(0, "8489")
        self.p2p_input_to.grid(row=1, column=3, sticky=W)

        self.p2p_label_alert = Label(self, anchor=W)
        self.p2p_label_alert.grid(row=2, column=0, columnspan=4, sticky=W)

        self.p2p_button_start = Button(self)
        self.p2p_button_start["text"] = "Start scanning"
        self.p2p_button_start["command"] = self.p2p_scan
        self.p2p_button_start.grid(row=3, column=0, sticky=W)

    def p2p_scan(self):
        id_from = str(self.p2p_input_from.get())
        id_to = str(self.p2p_input_to.get())

        if self.check_from_to_input(id_from, id_to):
            p2p = kokos.DataController()
            id_range = p2p.build_id_range(id_from, id_to)

            if id_range:
                p2p.make_export(id_range)

    def check_from_to_input(self, id_from, id_to):
        self.p2p_label_alert["text"] = ""

        if id_from.isdigit() and id_to.isdigit():
            if id_from.__len__() == id_to.__len__():
                if int(id_from) < int(id_to):
                    return True
                else:
                    self.p2p_label_alert["text"] = "From ID cannot be bigger or the same value as To ID."
                    self.p2p_label_alert["fg"] = "red"
                    return False
            else:
                self.p2p_label_alert["text"] = "The ID values are not equal in length."
                self.p2p_label_alert["fg"] = "red"
                return False
        else:
            self.p2p_label_alert["text"] = "The ID values are not numbers."
            self.p2p_label_alert["fg"] = "red"
            return False

