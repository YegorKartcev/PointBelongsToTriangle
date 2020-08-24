#! python 3

import tkinter as tk
import tkinter.font as tkFont


class Window(tk.Frame):

    def __init__(self, master=None):
        tk.Frame.__init__(self, master)   
        self.master = master
        self.customFont1 = tkFont.Font(family="Times New Roman", size=14) 
        self.init_window()
        
       
    def init_window(self):
        window.title("PointBelongsToTriangle")
#        window.resizable(width = False, height = False)
        window.geometry('600x650')
        
        label0 = tk.Label(text = "Welcome to PointBelongsToTriangle app!", font=self.customFont1)
        label0.grid(column = 2, row = 0)
       
 
window = tk.Tk()
app = Window(window)
window.mainloop()











