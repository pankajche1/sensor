import tkinter as tk
import tkinter.ttk as ttk
from tkinter import filedialog
from views.page import Page
#import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)

class HomePage(Page):
    '''
    
    '''
    def set_layout(self):
        #super().set_layout()
        #print('creating start page...')
        row = 0
        header = tk.Frame(self)
        header.pack()
        ttk.Label(header, text='Welcome!', font = self.font_style) \
                               .grid(row=0, column=1)
        #self.lbl_last_login = ttk.Label(header, text='Last Login:', font = self.font_style)
        #self.lbl_last_login.grid(row=0, column=1)
        self.menu_frame = tk.Frame(self)
        self.menu_frame.pack()

    def add_button_to_nav_menu(self, btn_text, page_title):
        def command(x = page_title):
            #return self.main_cont.show_page(x)
            return self.conts[0].show_page(x)
        i_row = len(self.menu_frame.winfo_children())
        tk.Button(self.menu_frame, text=btn_text, width=25 
                   , command = command).grid(row=i_row, column=0, padx=10, pady=5)
    
        
