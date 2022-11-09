import tkinter as tk
import tkinter.ttk as ttk
from views.page import Page
from tkinter import filedialog
#import cv2
from PIL import ImageTk, Image
#import numpy as np
#import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)

class CalibrationPage(Page):

    def set_layout(self):
        super().set_header_layout('Calibration Section')
        header = tk.Frame(self)
        header.pack(side = "top", fill = "both", expand = True)
        
        #super().set_layout()
        #print('creating start page...')
        row = 0
        #header = tk.Frame(self)
        #header.pack()
        #ttk.Label(header, text='Welcome!', font = self.font_style) \
        #                       .grid(row=0, column=1)
        body = tk.Frame(self)
        body.pack()
        # left and right panes:
        frame_left = tk.Frame(body)
        frame_left.grid(row=0, column=0, padx=10, pady=10)
        self.frame_right = frame_right = tk.Frame(body)
        frame_right.grid(row=0, column=1, padx=10, pady=10)
        frame_bottom = tk.Frame(body)
        frame_bottom.grid(row=1, column=0, columnspan=2, sticky=tk.NW)
        self.populate_left_pane(frame_left)
        self.populate_right_pane(frame_right)
        self.populate_bottom_pane(frame_bottom)

    def populate_left_pane(self, parent):
        row = 0
        # open button:
        #    change the function to select_image after dev
        btn_open_image = ttk.Button(parent, text="Open Image..."
                                    , command = self.conts[1].select_image_btn_clicked)
        btn_open_image.grid(row=row, column=0)
        # threshold:
        #   threshold 1:
        row += 1
        frame_threshold = tk.LabelFrame(parent, text = 'Threshold')
        frame_threshold.grid(row=row, column=0, padx=10, pady=10)
        ttk.Label(frame_threshold, text='Low:').grid(row=0, column=0, sticky=tk.E)
        self.thr_val1 = tk.IntVar()
        self.thr_val1.set(self.conts[1].threshold1)
        self.slider_thr_val1 = ttk.Scale(frame_threshold, length=200, from_=0, to=255, orient='horizontal'
                                          , command=self.update_threshold1
                                          , variable=self.thr_val1
                                          , state = 'disabled')
        self.slider_thr_val1.grid(row=0, column=1, padx=5, pady=5)
        
        self.lbl_thr_val1 = ttk.Label(frame_threshold, text=str(self.thr_val1.get()))
        self.lbl_thr_val1.grid(row=0, column=2, sticky=tk.W)
       
        #   threshold 2:
        #row += 1
        ttk.Label(frame_threshold, text='Max:').grid(row=1, column=0, sticky=tk.E)
        self.thr_val2 = tk.IntVar() 
        self.thr_val2.set(self.conts[1].threshold2)
        self.slider_thr_val2 = ttk.Scale(frame_threshold, length=200, from_=0, to=255, orient='horizontal'
                                          , command=self.update_threshold2
                                          , variable=self.thr_val2
                                          , state = 'disabled')
        self.slider_thr_val2.grid(row=1, column=1, padx=5, pady=5)
        
        self.lbl_thr_val2 = ttk.Label(frame_threshold, text=str(self.thr_val2.get()))
        self.lbl_thr_val2.grid(row=1, column=2, sticky=tk.W)
        btn_submit = ttk.Button(frame_threshold, text="Set", command = self.submit_btn_clicked)
        btn_submit.grid(row=2, column=2, padx=5, pady=5)

        #        # radius of circle to draw:
        #        row += 1
        #        ttk.Label(parent, text='Radius').grid(row=3, column=0)
        #        self.radius_val = tk.IntVar() 
        #        self.radius_val.set(10)
        #        slider_radius_val = ttk.Scale(parent, length=200, from_=0, to=50, orient='horizontal'
        #                                          , command=self.update_circle_radius
        #                                          , variable=self.radius_val
        #                                          , state = 'disabled')
        #        slider_radius_val.grid(row=row, column=1)
        #        
        #        self.lbl_radius_val = ttk.Label(parent, text=str(self.radius_val.get()))
        #        self.lbl_radius_val.grid(row=row, column=2)
        #        # varible to change the min num of edges for a polygon to be a circle:
        #        row += 1
        #        ttk.Label(parent, text='Circle Edges').grid(row=row, column=0)
        #        self.circle_min_edges_val = tk.StringVar()
        #        self.circle_min_edges_val.set(str(self.conts[1].circle_min_edges))
        #        frame_circle_min_edges = tk.Frame(parent)
        #        frame_circle_min_edges.grid(row=row, column=1)
        #        entry_circle_min_edges = ttk.Entry(frame_circle_min_edges
        #                                           , width = 5
        #                                           , textvariable = self.circle_min_edges_val)
        #        entry_circle_min_edges.grid(row=0, column=0)
        #        btn_circle_min_edges = ttk.Button(frame_circle_min_edges, text="Set"
        #                                           , command = self.set_circle_min_edges_btn_clicked)
        #        btn_circle_min_edges.grid(row=0, column=1)
        #        # for attaching concentration data to circle:
        #        row += 1
        #        ttk.Label(parent, text='ppm:').grid(row=5, column=0)
        #        self.concen_val = tk.StringVar()
        #        self.concen_val.set(str(0))
        #        frame_concen = tk.Frame(parent)
        #        frame_concen.grid(row=row, column=1)
        #        entry_concen = ttk.Entry(frame_concen
        #                                           , width = 5
        #                                           , textvariable = self.concen_val)
        #        entry_concen.grid(row=0, column=0)
        #        btn_set_concen = ttk.Button(frame_concen, text="Set"
        #                                           , command = self.set_concen_btn_clicked)
        #        btn_set_concen.grid(row=0, column=1)
        #        
        #        # button for concentration:
        #row += 1
        row += 1
        btn_cycle =  ttk.Button(parent, text="Cycle", command = self.cycle_btn_clicked)
        
        btn_cycle.grid(row=row, column=0)
        row += 1
        btn_read_concn_file =  ttk.Button(parent
                                          , text="Open concn. file..."
                                          , command = self.conts[1].read_concn_file_btn_clicked)
        btn_read_concn_file.grid(row=row, column=0)
        row += 1
        frame_concn = tk.Frame(parent)
        frame_concn.grid(row=row, column=0)
        self.om_concn_var = tk.StringVar(self)
        options = ['Nil']
        self.om_concn_var.set(options[0])
        ttk.Label(frame_concn, text='Concn:') \
                           .grid(row=0, column=0)
        self.om_concen = tk.OptionMenu(frame_concn
                                     , self.om_concn_var
                                     , *options
                                     #, command = self.cont.om_assets_clicked
                                     )
        self.om_concen.grid(row=0, column=1, padx=10, pady=10, sticky=tk.W)
        btn_link_concen = ttk.Button(frame_concn, text="Link"
                                           , command = self.link_concen_btn_clicked)
        btn_link_concen.grid(row=0, column=2)
        row += 1
        btn_purge_data = ttk.Button(parent, text="Purge data..."
                                           , command = self.conts[1].purge_data_btn_clicked)
        btn_purge_data.grid(row=row, column=0)

    def populate_right_pane(self, parent):
        # right pane:
        self.lbl_img = ttk.Label(parent, text='main image here')
        self.lbl_img.grid(row = 0, column = 0)
        self.lbl_img2 = ttk.Label(parent, text='image 2 here')
        self.lbl_img2.grid(row = 1, column = 0)        
        self.lbl_img3 = ttk.Label(parent, text='image 3 here')
        self.lbl_img3.grid(row = 2, column = 0)        
        self.lbl_img4 = ttk.Label(parent, text='image 4 here')
        self.lbl_img4.grid(row = 3, column = 0)        
        self.lbl_img5 = ttk.Label(parent, text='image 5 here')
        self.lbl_img5.grid(row = 4, column = 0)
        self.lbl_img6 = ttk.Label(parent, text='Image with concentrations')
        self.lbl_img6.grid(row = 5, column = 0)        
        
        
    def populate_bottom_pane(self, parent):
        #self.result_var = tk.StringVar()
        #self.result_var.set('Result\nhere\nmore result is awaited here and it is required to do it.')        
        #msg_result = tk.Message(parent, width=400, aspect=400
        #                      , bg='#000000', fg='#FFFFFF'
        #                      , textvariable=self.result_var
        #                      , justify=tk.LEFT
        #                      )
        #
        #msg_result.grid(row=1, column=0, padx=10, pady=10, sticky=tk.NW)
        # text:
        self.txt_result = tk.Text(parent, width=50, bg='#000000', fg='#FFFFFF')
        self.txt_result.grid(row=2, column=0, padx=10, pady=10)

    def display_result(self, text):
        self.txt_result.delete(1.0,"end")
        self.txt_result.insert(1.0, text)
        
    def select_image_dev(self):
        '''
        this method is to test other things easily so
        that you don't have to select the img again again on testing
        '''
        filename = './image-01.png'
        self.read_image(filename)

    def get_image_filename_from_user(self):
        return filedialog.askopenfilename(initialdir = "/Home/",
                                          title = "Select a File",
                                          filetypes = (("Image files",
                                                        "*.png*"),
                                                       ("all files",
                                                        "*.*")))
        
    def read_image(self, filename):
        self.image = cv2.imread(filename)
        self.is_image_read = True
        self.display_image(self.image, 1)
        self.gray_img = self.get_bgr2gray(self.image)
        self.display_image(self.gray_img, 2)
        self.process_image()

    def update_threshold1(self, event):
        self.conts[1].set_threshold1(self.thr_val1.get())

    def update_threshold2(self, event):
        self.conts[1].set_threshold2(self.thr_val2.get())

    def update_threshold1_view(self, val):
        self.lbl_thr_val1['text'] = val
        
    def update_threshold2_view(self, val):
        self.lbl_thr_val2['text'] = val

    def display_image(self, image_array, container_id = 1):
        img_data = Image.fromarray(image_array)
        img_w, img_h = img_data.size
        # resize the img so that it fits in the gui:
        max_w = 500 # px
        if img_w > max_w:
            frac = max_w/img_w
            resized_dimensions = (int(img_w * frac), int(img_h * frac))
            resized_data = img_data.resize(resized_dimensions)
            imgtk = ImageTk.PhotoImage(resized_data)
        else:
            imgtk = ImageTk.PhotoImage(img_data)
        if container_id == 1:
            self.lbl_img.configure(image = imgtk)
            self.lbl_img.image = imgtk
        elif container_id == 2:
            self.lbl_img2.configure(image = imgtk)
            self.lbl_img2.image = imgtk
        elif container_id == 3:
            self.lbl_img3.configure(image = imgtk)
            self.lbl_img3.image = imgtk
        elif container_id == 4:
            self.lbl_img4.configure(image = imgtk)
            self.lbl_img4.image = imgtk
        elif container_id == 5:
            self.lbl_img5.configure(image = imgtk)
            self.lbl_img5.image = imgtk
        elif container_id == 6:
            self.lbl_img6.configure(image = imgtk)
            self.lbl_img6.image = imgtk

    def clear_image(self, container_id):
        '''

        '''
        target_container = None
        if container_id == 1:
            target_container = self.lbl_img
        elif container_id == 2:
            target_container = self.lbl_img2
        elif container_id == 3:
            target_container = self.lbl_img3
        elif container_id == 4:
            target_container = self.lbl_img4
        elif container_id == 5:
            target_container = self.lbl_img5 
        elif container_id == 6:
            target_container = self.lbl_img6
        target_container.configure(image = '')

    def submit_btn_clicked(self):
        self.conts[1].submit_btn_clicked()
        

    
    def update_circle_radius(self, event):
        self.lbl_radius_val['text'] = str(self.radius_val.get())
        
    def set_sliders_states(self, val):
        self.slider_thr_val1['state'] = val
        self.slider_thr_val2['state'] = val        

    def set_circle_min_edges_btn_clicked(self):
        self.conts[1].set_circle_min_edges_btn_clicked()

    def get_circle_min_edges_val(self):
        return self.circle_min_edges_val.get()

    def cycle_btn_clicked(self):
        self.conts[1].cycle_btn_clicked()

    def set_concen_btn_clicked(self):
        #self.conts[1].set_concen_btn_clicked(self.concen_val.get())
        self.plot()

    def plot(self):
        # the figure that will contain the plot
        fig = Figure(figsize=(5,5), dpi = 100)
        # list of squares
        y = [i**2 for i in range(101)]
        # adding the subplot
        plot1 = fig.add_subplot(111)
        # plotting the graph
        plot1.plot(y)
        # creating the Tkinter canvas
        # containing the Matplotlib figure
        canvas = FigureCanvasTkAgg(fig, master = self.frame_right)
        canvas.draw()
        # placing the canvas on the Tkinter window
        #canvas.get_tk_widget().pack()
        canvas.get_tk_widget().grid(row=0, column=0)
        # creating the Matplotlib toolbar
        toolbar = NavigationToolbar2Tk(canvas, self.frame_right)
        toolbar.update()
        # placing the toolbar on the Tkinter window
        #canvas.get_tk_widget().pack()
        canvas.get_tk_widget().grid(row=1, column=0)
        
    def get_concn_file_name_from_user(self):
        return filedialog.askopenfilename(initialdir = "/Home/",
                                          title = "Select a concn. file",
                                          filetypes = (("csv files",
                                                        "*.csv*"),
                                                       ("all files",
                                                        "*.*")))
    
        
    def link_concen_btn_clicked(self):
        self.conts[1].link_concen_btn_clicked(self.om_concn_var.get())

    def update_om_concen_values(self, opts):
        menu = self.om_concen["menu"]
        #print(type(menu))
        #print(menu)
        menu.delete(0, "end")
        for string in opts:
            menu.add_command(label=string, 
                             command=lambda value=string: self.om_concn_var.set(value))
        self.om_concn_var.set(opts[0])


