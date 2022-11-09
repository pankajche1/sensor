#!/usr/bin/env python3
import sys
import tkinter as tk
import tkinter.ttk as ttk
# import filedialog module
from tkinter import filedialog
from controllers.main_cont import MainController
from views.menubar import Menubar
from views.views_manager import ViewsManager
from models.data import Data
FONT1 = ("Verdana", 12)

class App(tk.Tk):

    def __init__(self):
        super().__init__()
        windowWidth = 1200
        windowHeight = 600
        self.title('Image Analysis Sensor')
        # Gets both half the screen width/height and window width/height
        positionRight = int(self.winfo_screenwidth()/2 - windowWidth/2)
        positionDown = int(self.winfo_screenheight()/2 - windowHeight/2)

        # Positions the window in the center of the page.
        # https://www.geeksforgeeks.org/python-geometry-method-in-tkinter/
        self.geometry("{}x{}+{}+{}".format(windowWidth, windowHeight, positionRight, positionDown))
        self._add_mouse_bindings()        
        menubar = Menubar(self)
        main_container = tk.Frame(self)
        main_container.pack(side = "top", fill = "both", expand = True, padx=10, pady=10)
        # STEP 2
        self.canvas = canvas = tk.Canvas(main_container)
        # STEP 3
        scrollbar_vert = ttk.Scrollbar(main_container, orient="vertical", command=canvas.yview)
        scrollbar_horiz = ttk.Scrollbar(main_container, orient="horizontal", command=canvas.xview)
        # STEP 4
        scrollable_frame = tk.Frame(canvas)
        #scrollable_frame.pack(side = "top", fill = "both", expand = True)
        scrollable_frame.pack(side="top", padx=10, pady=10)
        #scrollable_frame.grid(row=0, column=0, padx=10, pady=10)
        #scrollable_frame.grid_rowconfigure(0, weight = 1)
        #scrollable_frame.grid_columnconfigure(0, weight = 1)        
        scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        # STEP 6 Next up we have to tell the canvas to actually draw the scrollable_frame inside itself:
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar_vert.set, xscrollcommand=scrollbar_horiz.set)
        data = Data()
        self.main_cont = mc = MainController()
        mc.set_views_manager(ViewsManager(scrollable_frame, FONT1))
        mc.data = data
        scrollbar_vert.pack(side="right", fill="y")
        scrollbar_horiz.pack(side="bottom", fill="x")        
        canvas.pack(side="left", fill="both", expand=True, padx=10, pady=10)   # 'left' for scrollbars ok
        #mc.go()
        mc.show_page('home page')


    def _add_mouse_bindings(self):
        self.bind('<Control-q>', self.quit_app)
        self.bind('<Control-w>', self.quit_app)
        #self.bind('<4>', lambda event : self.canvas.yview('scroll', -1, 'units'))
        #self.bind('<5>', lambda event : self.canvas.yview('scroll', 1, 'units'))        
        #self.bind('<Shift-4>', lambda event : self.canvas.xview('scroll', -1, 'units'))
        #self.bind('<Shift-5>', lambda event : self.canvas.xview('scroll', 1, 'units'))        
        
    def quit_app_from_menu(self):
        self.destroy()
        
    def quit_app(self, e):
        self.destroy()

def on_closing():
    app.destroy()
    
if __name__=="__main__":
    app = App()
    app.protocol("WM_DELETE_WINDOW", on_closing)      
    app.mainloop()




