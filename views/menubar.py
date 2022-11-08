from tkinter import Menu  
class Menubar(Menu):
        def __init__(self, parent):
            super().__init__(parent)

            #menubar = Menu(self)
        
            file = Menu(self, tearoff=0)  
            file.add_command(label="New")  
            file.add_command(label="Open")  
            file.add_command(label="Save")  
            file.add_command(label="Save as...")  
            file.add_command(label="Close")  
  
            file.add_separator()  
  
            #file.add_command(label="Exit", command=self.quit)  
            #file.add_command(label="Exit", command=self.quit, accelerator="Ctrl+Q")
            file.add_command(label="Exit", command=parent.quit_app_from_menu, accelerator="Ctrl+Q")
  
            self.add_cascade(label="File", menu=file)  
            edit = Menu(self, tearoff=0)  
            edit.add_command(label="Undo")  
  
            edit.add_separator()  
  
            edit.add_command(label="Cut")  
            edit.add_command(label="Copy")  
            edit.add_command(label="Paste")  
            edit.add_command(label="Delete")  
            edit.add_command(label="Select All")  
  
            self.add_cascade(label="Edit", menu=edit)  
            help = Menu(self, tearoff=0)  
            help.add_command(label="About")  
            self.add_cascade(label="Help", menu=help)  
        
            parent.config(menu=self)
