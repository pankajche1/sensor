class AnalysisController:
    '''
    
    '''
    def go(self):
    
    
        if self.view.is_layout_set():
            self.view.clear_data()
        else:
            self.view.set_layout()
            self.populate_page()
            self.view.set_is_layout_set(True)       

    def populate_page(self):
        pass

