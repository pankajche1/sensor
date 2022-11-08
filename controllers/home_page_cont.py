class HomePageController:
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
        for item in self.data.get_navigation_menu_data():
            #print('StartPageCont::populate_pate:{} {}'.format(item[0], item[1]))
            self.view.add_button_to_nav_menu(item[0], item[1])                                 

    
