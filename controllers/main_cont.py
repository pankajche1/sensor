import gc

class MainController:
    cur_page = None
    image = None
    def __init__(self):
        pass

    def go(self):
        print('ok')

    def set_views_manager(self, manager):
        self.views_manager = manager
        
    def show_page(self, page_name):
        '''
           sss     
        '''

        if self.cur_page:

            self.cur_page.pack_forget()
            self.cur_page.destroy()
            self.cur_page = None
            self.views_manager.remove_imported_modules()
        # to know objects in memory:
        objects = gc.get_objects()  
        #1 create the page object:
        self.views_manager.clear_page_containter()
        objs = self.views_manager.get_page(page_name)
        if not objs:
            return
        self.cur_page = objs[0]
        self.cur_page.pack()
        cont = objs[1] # page controller
        #print('MainCont::show_page():sys.modules:{}'.format(sys.modules))
        #cont.now = datetime.now()
        cont.view = self.cur_page
        cont.data = self.data
        self.cur_page.conts = []
        self.cur_page.add_controller(self)
        self.cur_page.add_controller(cont)
        cont.go()            
        
