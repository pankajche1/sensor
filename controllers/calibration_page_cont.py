import csv
import cv2
from PIL import ImageTk, Image
import numpy as np
import matplotlib.pyplot as plt
from models.circle import Circle
#from matplotlib.figure import Figure
#from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)

class CalibrationController:
    '''
    
    '''
    main_cont = None
    threshold1 = 127
    threshold2 = 255
    concentrations = [0.0, 1.0, 2.5, 3.0
                      , 5.0, 10.0, 25.0, 50.0, 100.0]
    ppms = [100.0, 50.0, 25.0, 10.0, 5.0, 3.0, 2.5, 1.0, 0.0]
    # for being a circle a polygon should have more than this:
    circle_min_edges = 6
    circles = [] # object to store target pixels color data
    i_circle = 0 # target circle
    image = None
    def __init__(self):
        '''
        
        '''
        pass
        
    def go(self):
    
    
        if self.view.is_layout_set():
            self.view.clear_data()
        else:
            self.view.set_layout()
            self.populate_page()
            self.view.set_is_layout_set(True)       

    def populate_page(self):
        pass

    def process_concn_file(self):
        #self.concn_file_path = res

        csvfile = open(self.concn_file_path, 'r')
        reader = csv.reader(csvfile)
        concentrations = []
        for row in reader:
            n = len(row)
            concentrations.append(float(row[0].strip()))
        csvfile.close()    
        #print(concentrations)
        self.view.update_om_concen_values(concentrations)
            

    def read_image(self):
        self.image = cv2.imread(self.image_path)
        #self.is_image_read = True
        # 2nd arg is container id where the img is to be displayed
        self.view.display_image(self.image, 1)
        self.gray_image = self.get_bgr2gray(self.image)
        self.view.display_image(self.gray_image, 2)
        #self.process_image()

    def get_bgr2gray(self, image):
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        return gray

    def process_image(self):
        self.read_image()
        self.process_image2()
        self.view.set_sliders_states('active')

    def process_image2(self):
        binary = self.get_threshold()
        self.contours = self.get_contours(binary)
        contours_image = self.get_contours_image()
        self.view.display_image(contours_image, 3)
        
    def get_threshold(self):
        _, binary = cv2.threshold(self.gray_image
                         , self.threshold1
                         , self.threshold2
                         , cv2.THRESH_BINARY_INV)
        return binary

    def set_threshold1(self, val):
        self.threshold1 = val
        self.view.update_threshold1_view(self.threshold1)
        self.process_image2()

    def set_threshold2(self, val):
        self.threshold2 = val
        self.view.update_threshold2_view(self.threshold2)
        self.process_image2()
        
    def get_contours(self, binary):        
        # find the contours from the thresholded image
        contours, _ = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        return contours


    def get_contours_image(self):
        # 3rd arg: -1 to draw all the contours
        # 5th arg: thickness of line, -1 to fill the inside
        contour_color = (255, 0, 0) # RGB OK
        contour_color = (255, 255, 0) # RGB OK
        image_copy = self.image.copy()
        for i_contour in range(0, len(self.contours)):
            if i_contour == 0: # this is the whole image so bypass
                #cv2.drawContours(image_copy, contours, i_contour, (0, 255, 255), -1)
                continue
            cv2.drawContours(image_copy, self.contours, i_contour, contour_color, -1)
        return image_copy
    
        
    def select_image_btn_clicked(self):
        # get target image path from user
        #  returns an empty tuple if user cancels the file selection dialog
        #  returns the file path as string if user selects an image file
        #  so if len() is zero then user has not selected anything
        res = self.view.get_image_filename_from_user()
        if len(res) > 0:
            self.image_path = res
            # now start processing the image:
            # clear earlier data:
            self.clear_data()
            self.process_image()
        else:
            print('no image selected')
                
    def submit_btn_clicked(self):
        if self.image is None:
            self.view.show_msgbox("No image selected", "Please open an image for processing", "error")
            return
        final = np.zeros(self.image.shape, np.uint8)
        mask = np.zeros(self.gray_image.shape, np.uint8)
        black_image = np.zeros(self.image.shape, np.uint8)
        #image2 = np.zeros(image.shape, np.uint8)
        self.circles = []
        for i_contour in range(0, len(self.contours)):
            contour = self.contours[i_contour]
            # cv2.approxPloyDP() function to approximate the shape
            approx = cv2.approxPolyDP(
                contour, 0.01 * cv2.arcLength(contour, True), True)
            if len(approx) > self.circle_min_edges:
                # finding center point of shape
                M = cv2.moments(contour)
                if M['m00'] != 0.0:
                    x = int(M['m10']/M['m00'])
                    y = int(M['m01']/M['m00'])
                self.circles.append(Circle(x, y))
        #print("len(circles):{}".format(len(self.circles)))
        color = 150
        radius = 10
        thickness = -1
        image_copy = self.image.copy()
        if len(self.circles) == 0:
            self.view.show_msgbox("No shape found", "No shape found for display", "error")
            return
        
        for circle in self.circles:
            # the color data from the src img:
            circle.indices = []
            self.set_circle_data(circle)
            self.draw_contours_from_data(image_copy, circle)
        self.view.display_image(image_copy, 4)
        # displays a circle:
        circle = self.circles[self.i_circle]
        self.display_cur_circle(circle)
        # image with concentrations:
        self.image_with_concen = self.image.copy()
        self.view.display_image(self.image_with_concen, 6)
        

    def draw_contours_from_data(self, image, circle):
        #print("len(circle.indices):{}".format(len(circle.indices[0])))
        for i in range(0, len(circle.indices[0])):
            # color is RGB
            image[circle.indices[0][i]][circle.indices[1][i]] = (0, 0, 255)

    def set_circle_min_edges_btn_clicked(self):
        self.circle_min_edges = int(self.view.get_circle_min_edges_val())
        #print(self.circle_min_edges)
        self.process_image2()
        
    def set_circle_data(self, circle):
        '''
         extracts the desired color data fro src img and puts it in 
         the circle object
        '''
        color = 150
        radius = 10
        thickness = -1
        # mask image:
        black_image = np.zeros(self.image.shape, np.uint8)
        # draw on this black image the target circle:
        cv2.circle(black_image, (circle.x, circle.y), radius, color, thickness )
        # get the indices (x, y, color) of this circle:
        circle.indices = np.where(black_image == color)
        circle.channels = []
        for i in range(0, len(circle.indices[0])):
            channel = self.image[circle.indices[0][i]][circle.indices[1][i]]
            circle.channels.append(channel)

        gray_scale_values = []
        simple_mean_values = []
        sum_R_values = 0
        sum_G_values = 0
        sum_B_values = 0
        for i in range(0, len(circle.channels)):
            gray_scale_values.append(self.get_gray_scale_value(circle.channels[i]))
            simple_mean_values.append(self.get_channels_mean(circle.channels[i]))
            sum_R_values += circle.channels[i][0]
            sum_G_values += circle.channels[i][1]
            sum_B_values += circle.channels[i][2]
        sum = 0
        sum2 = 0
        n_channels = 0
        #print("len(gray_scale_values):{}".format(len(gray_scale_values)))
        for i in range(0, len(gray_scale_values)):
            sum += gray_scale_values[i]
            sum2 += simple_mean_values[i]
            n_channels += 1
            #if gray_scale_values[i] > 0:
            #    sum += gray_scale_values[i]
            #    n_channels += 1
        circle.mean = sum/n_channels
        circle.simple_mean = sum2/n_channels
        circle.R_mean = sum_R_values/n_channels
        circle.G_mean = sum_G_values/n_channels
        circle.B_mean = sum_B_values/n_channels
            


    def get_gray_scale_value(self, channel):
        return 0.299* channel[2] + 0.587 * channel[1] + 0.114 * channel[0]

    def get_channels_mean(self, channel):
        return channel[2]/3.0 + channel[1]/3.0 + channel[0]/3.0

    def display_cur_circle(self, circle):
        '''
        displays the current selected circle
        '''
        # draw this circle on fake image:
        # a fake image to display circles:
        image_copy = self.image.copy()
        self.draw_contours_from_data(image_copy, circle)
        str_result =  "       mean:  {:<.2f} \n\n".format(circle.mean)
        str_result += "simple mean:  {:<.2f} \n\n".format(circle.simple_mean)
        str_result += "     R mean:  {:<.2f} \n\n".format(circle.R_mean)
        str_result += "     G mean:  {:<.2f} \n\n".format(circle.G_mean)
        str_result += "     B mean:  {:<.2f} \n\n".format(circle.B_mean)
        self.view.display_image(image_copy, 5)
        self.view.display_result(str_result)

        
    def cycle_btn_clicked(self):
        if len(self.circles) == 0:
            self.view.show_msgbox('no data!', 'no data found', 'error')
            return
        self.i_circle += 1
        if self.i_circle > len(self.circles) - 1:
            self.i_circle = 0
        # target circle:
        circle = self.circles[self.i_circle]
        self.display_cur_circle(circle)

    def set_concen_btn_clicked(self, concen):
        circle = self.circles[self.i_circle]
        circle.concen = float(concen)
        print("concent {} attached...".format(circle.concen))
        
            
    def read_concn_file_btn_clicked(self):
        res = self.view.get_concn_file_name_from_user()
        if len(res) > 0:
            self.concn_file_path = res
            # now start processing the image:
            self.process_concn_file()
        else:
            print('no csv file selected')
        
    def link_concen_btn_clicked(self, concen_selected):
        #print(concen_selected)
        if len(self.circles) == 0:
            self.view.show_msgbox("No pixels Error", "No shapes found for linking!", 'error')
            return
        if len(concen_selected) == 0 or concen_selected == 'Nil':
            self.view.show_msgbox("No concentrations Error", "No concentrations found for linking!", 'error')
            return
            
        circle = self.circles[self.i_circle]
        circle.concen = float(concen_selected)
        print("concent {} attached...".format(circle.concen))
        # show it on display:
        cv2.putText(self.image_with_concen, str(circle.concen), (circle.x, circle.y + 10),
                         cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255, 255, 0), 1)
        self.view.display_image(self.image_with_concen, 6)


    def clear_data(self):
        '''

        '''
        self.view.clear_image(1)
        self.view.clear_image(2)
        self.view.clear_image(3)
        self.view.clear_image(4)
        self.view.clear_image(5)
        self.view.clear_image(6)        
        # clear data:
        self.image = None
        self.gray_image = None
        self.contours = []
        self.circles = []
        self.concn_file_path = None
        self.view.update_om_concen_values(['Nil'])
        
    def purge_data_btn_clicked(self):
        res = self.view.show_msgbox("Purge data", "Do you want to purge all data?", "yesno")
        if res:
            self.clear_data()

