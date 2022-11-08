import sys

class ViewsManager:
    '''
    
    '''
    cur_view_module = None
    cur_cont_module = None
    # It is necessary to give this ways:
    #    (('item', 'item') , ) the '.' is important to be there. other wise filter cycling through the ('item', 'item') 
    classes = (
                ('home page', 'home_page', 'HomePage', 'home_page_cont', 'HomePageController' )
                , ('calibration page', 'calibration_page', 'CalibrationPage', 'calibration_page_cont', 'CalibrationController' )
                , ('analysis page', 'analysis_page', 'AnalysisPage', 'analysis_page_cont', 'AnalysisController' )
              )

    def __init__(self, frame, font):
        self.frame = frame
        self.font = font


    def get_page(self, page_name):
        '''
        returns a tuple containing View and Controller object
        '''
        # the following line retrieves the tuple which contains the given page title:
        # list(filter(lambda x:page_title in x, ViewsManager.classes)) # checks all the four elements of the tuple
        self.page_name = page_name
        cls_data = list(filter(lambda x:page_name in x[0], ViewsManager.classes))
        if len(cls_data) == 0:
            # no module found
            print("No '{}' found in views/views_manager/get_page()...".format(page_name))
            # TODO show a default error page here (web page style)
            return None
        
        module_v = 'views.' + cls_data[0][1]
        #print(mod)
        view_module = __import__(module_v, fromlist=[cls_data[0][2]])
        self.cur_view_module = module_v
        

        #print(cont_module)
        View = getattr(view_module, cls_data[0][2])
        module_c = 'controllers.' + cls_data[0][3]
        self.cur_cont_module = module_c
        #print(mod)
        cont_module = __import__(module_c, fromlist=[cls_data[0][4]])
        #print(cont_module)
        Cont = getattr(cont_module, cls_data[0][4])
        return (View(self.frame, cls_data[0][0], self.font), Cont())
     
    def clear_page_containter(self):
        #print('ViewManager::clear_page_container()')
        for widget in self.frame.winfo_children():
            #print('ViewManager::clear_page_container() type widget:\n\t\t{}'.format(type(widget)))
            widget.destroy()  
   
    def remove_imported_modules(self):
        '''
        import sys
        import requests


        print(requests.get)


        del sys.modules['requests']
        del requests


        print(requests.get)
        '''
        #print('view manager:: sys.module:{}'.format(sys.modules[self.cur_view_module]))
        del sys.modules[self.cur_view_module]
        del self.cur_view_module
        del sys.modules[self.cur_cont_module]
        del self.cur_cont_module
        

                


        

