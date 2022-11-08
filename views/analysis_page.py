import tkinter as tk
import tkinter.ttk as ttk
from views.page import Page
from tkinter import filedialog
#import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)

class AnalysisPage(Page):

    def set_layout(self):
        super().set_header_layout('Analysis Section')
        header = tk.Frame(self)
        header.pack(side = "top", fill = "both", expand = True)
        row = 0
        body = tk.Frame(self)
        body.pack()

