import numpy as np
from matplotlib import pyplot as plt
import cv2

class Circle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
def get_gray_scale_value(channel):
    return 0.299* channel[2] + 0.587 * channel[1] + 0.114 * channel[0]

def show_channel_mean(image, image2, black_image, circles, i_circle):
    color = 150
    circle = circles[i_circle]
    radius = 10
    thickness = -1
    
    cv2.circle(black_image, (circle.x, circle.y), radius, color, thickness )
    print("circle: x:{}, y:{}".format(circle.x, circle.y))
    #cv2.circle(black_image, (circle.x, circle.y), 2, (0, 255, 0), thickness )

    indices = np.where(black_image == color)
    print("len(indices):{}".format(len(indices[0])))
    #print("type(black_image):{}".format(type(black_image)))
    #print("type(image):{}".format(type(image)))
    channels = []
    for i in range(0, len(indices[0])):
        channel = image[indices[0][i]][indices[1][i]]
        channels.append(channel)
        #if i >=50 and i <=1000:
        #if i >=0 and i < len(indices[0]):
        if i >=0 and i < 5:
            #pass
            # B G R values:
            print("channel (BGR):{}".format(channel))
            #print("x:{}, y:{}, color:{}".format(indices[0][i], indices[1][i], indices[2]))
            #cv2.circle(black_image,(indices[1][i],indices[0][i]), 2, (0, 0, 255), -1 )
            #cv2.circle(image,(indices[1][i],indices[0][i]), 2, (0, 0, 255), -1 )
    #cv2.imshow('Black Image', black_image)
    print("n channels:{}".format(len(channels)))
    gray_scale_values = []
    for i in range(0, len(channels)):
        gray_scale_values.append(get_gray_scale_value(channels[i]))
    sum = 0
    n_channels = 0
    print("len(gray_scale_values):{}".format(len(gray_scale_values)))
    for i in range(0, len(gray_scale_values)):
        sum += gray_scale_values[i]
        n_channels += 1
        #if gray_scale_values[i] > 0:
        #    sum += gray_scale_values[i]
        #    n_channels += 1
    print("n_channels for mean:{}".format(n_channels))
    mean = sum/n_channels
    print("mean:{}".format(mean))
    cv2.circle(image2,(circle.x, circle.y), radius, (0, 0, 255), -1 )    
    cv2.putText(image2, str(mean)[0:4], (circle.x, circle.y + 10),
                         cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255, 255, 0), 1)

        
def main():
    images = ["Fe Sensor image1.png", "rect-01.png"
               , "Figure Digital colorimetric image-small-size.png"
               , "circles.png"]
    img_id = 2
    image = cv2.imread(images[img_id])
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    _, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)
    # find the contours from the thresholded image
    contours, _ = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # draw all contours
    #image = cv2.drawContours(image, contours, -1, (0, 255, 0), 2)    
    #image = cv2.drawContours(image, contours, 0, (255, 0, 0), -1)    
    final = np.zeros(image.shape, np.uint8)
    mask = np.zeros(gray.shape, np.uint8)
    black_image = np.zeros(image.shape, np.uint8)
    image2 = np.zeros(image.shape, np.uint8)
    #cv2.imshow('image', gray)
    print("len(contours):{}".format(len(contours)))
    
    i_contour = 0


    circles = []
    for i_contour in range(0, len(contours)):
        contour = contours[i_contour]
        # cv2.approxPloyDP() function to approximate the shape
        approx = cv2.approxPolyDP(
            contour, 0.01 * cv2.arcLength(contour, True), True)
        if len(approx) > 6:
            
            #print("circle")
            #cv2.drawContours(final, contours, i_contour, color, -1)

            # finding center point of shape
            M = cv2.moments(contour)
            if M['m00'] != 0.0:
                x = int(M['m10']/M['m00'])
                y = int(M['m01']/M['m00'])
            circles.append(Circle(x, y))
            #radius = 5
            #thickness = -1
            #cv2.circle(final, (x,y), radius, (255, 255, 0), thickness )
            #if i_circle == i_target_circle:
            #   cv2.circle(black_image, (x,y), radius, color, thickness )
            #i_circle += 1
            #cv2.circle(final, (x,y), 1, (255, 255, 0), 1 ) # center
            #cv2.putText(final, 'Cricle'+str(i_contour), (x, y),
            #            cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255, 255, 255), 1)

        #else:
            #print("no circle")
    print("len(circles):{}".format(len(circles)))
    i_target_circle = 0
    for i_circle in range(0, len(circles)):
        print("i_circle:{}".format(i_circle))
        show_channel_mean(image, image2, black_image, circles, i_circle)
        if i_circle == i_target_circle:
            pass
            #print("i_circle:{}".format(i_circle))
            #show_channel_mean(image, image2, black_image, circles, i_circle)
    
    cv2.imshow('Image2', image2)
    cv2.imshow('Image', image)    
    cv2.waitKey(0)
    


if __name__ == '__main__':
    main()
