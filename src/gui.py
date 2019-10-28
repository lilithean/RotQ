#!/usr/bin/env python
#
# Copyright (C) 2019 Xiaoyu Wang <xwang224@buffalo.edu>
#
# This file is part of Running on the Queue Job Manager
#
#            < gui.py >
# The graphic user interface of RotQ software
#

import Tkinter as tk

class Navbar(tk.Frame): pass

class Toolbar(tk.Frame): pass

class Statusbar(tk.Frame):

    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.label = tk.Label(self, borderwidth=1, relief='sunken', anchor='w')
        self.label.pack(fill='x')

    def set(self, format, *args):
        self.label.config(text=format % args)
        self.label.update_idletasks()

    def clear(self):
        self.label.config(text='')
        self.label.update_idletasks()


class Application(tk.Frame):

    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.master = master
        self.i = 1
        self.j = 1
        self.button = tk.Button(self, text='going up', command=self.going_up)
        self.statusbar = Statusbar(master)
        self.statusbar2 = Statusbar(master)
        self.growing_up()

        self.button.pack(side='top', fill=None)
        self.statusbar.pack(side='bottom', fill='x')
        self.statusbar2.pack(side='bottom', fill='x')


    def going_up(self):
        self.i += 1
        self.statusbar.set('%i', self.i)

    def growing_up(self):
        self.j += 1
        self.statusbar2.set('%i', self.j)
        self.master.after(100, self.growing_up)



if __name__ == "__main__":
    root = tk.Tk()
    Application(root).pack(side="top", fill="both", expand=True)
    root.mainloop()
