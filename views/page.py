import tkinter as tk
import tkinter.ttk as ttk
#from views.accounts_page import AccountsPage
#from views.expenses_page import ExpensesPage
#from views.accounts_page import AccountsPage



class Page(tk.Frame):
    '''
    
    '''
    title = None
    font_style = None
    _is_layout_set = False
    view = None
    tabs = []
    # controllers:
    conts = []
    #tab_frames = []
    
    def __init__(self, parent_container, title, font_style):
        '''
        
        '''
        super().__init__(parent_container)
        self.title = title
        self.font_style = font_style
        self.conts = [] # necessary otherwise other objects of this class are using this
   
    def add_controller(self, cont):
        #print('Page::add_controller() adding cont:{}'.format(type(cont)))
        self.conts.append(cont)

    def add_controller_to_tab(self, i_tab, cont):
        if i_tab < len(self.tabs):
            self.tabs[i_tab].conts.append(cont)    
        

    def set_layout(self):
        #print('Page.set_layout()...')
        pass
        
    def set_header_layout(self, header_text):
        frame1 = tk.Frame(self)
        frame1.pack(side = "top", fill = "both", expand = True)
        # home button
        self.home_button = tk.Button(frame1, text='Home', 
                      command= lambda : self.conts[0].show_page('home page'))
        self.home_button.grid(row=0, column=0, padx=10, pady=10)
        self.label = ttk.Label(frame1, text=header_text, font = self.font_style)
        self.label.grid(row=0, column=1)    

    def get_title(self):
        return self.title
        
    def set_is_layout_set(self, is_set):
        '''
        :param: is_set Boolean
        '''
        self._is_layout_set = is_set
        
    def is_layout_set(self):
        return self._is_layout_set
        
    def clear_data(self):
        pass
     
    def clear_tab_data(self, i_tab):
        '''
        clears data in given tab
        :param: i_tab : tab index
        '''
        if i_tab < len(self.tabs):
            self.tabs[i_tab].clear_data()
        
    def clear_layout(self):
        '''
        destroy all the widgets on this Frame
        '''
        for tab in self.tabs:
            tab.conts = []
            for w in tab.winfo_children():
                w.destroy()
        for widget in self.winfo_children():
            widget.destroy() 
            
    def show_msgbox(self, title, msg, type='info'):
        if type == 'error':
            return tk.messagebox.showerror(title, msg)
        elif type == 'info':
            return tk.messagebox.showinfo(title, msg)
        elif type == 'yesno':
            return tk.messagebox.askyesno(title, msg)            
        
        
        
          
