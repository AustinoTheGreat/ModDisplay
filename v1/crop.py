"""
Created on Fri Jun 12 10:46:20 2020
@author: joelbinu, AustinoTheGreat :)
"""
from PIL import Image

# taking an image and then adjusting it to the 1024 by 600 aspect ratio

# m1 is the left sensor
# m2 is the top sensor
def main(img, m1, m2, IMU):

    #image = Image.open("/home/pi/ModDisplay/Image repo/vector1.jpg")
    image = img

    width = image.size[0]
    height = image.size[1]

    def orientation(m1, m2):
        
        global image2
        global width
        global height
        if (m1 == 1) and (m2 == 1):
            
            image2 = image.resize((1024,600))
            width = image2.size[0]
            height = image2.size[1]
            crop(width/2, width, height/2, height)
            
        elif (m1 == 1) and (m2 == 0):
            
            image2 = image.resize((2028, 600))
            width = image2.size[0]
            height = image2.size[1]
            crop(width/2, width, 0 , height)
        
        elif (m1 == 0) and (m2 == 1):
            
            image2 = image.resize((1024, 1200))
            width = image2.size[0]
            height = image2.size[1]
            crop(0, width, height/2 , height)
            
        elif (m1 == 0) and (m2 == 0):
            
            image2 = image.resize((1024, 600))
            width = image2.size[0]
            height = image2.size[1]
            image2.show()
            
    def crop(left, right, top, bottom):
        im1 = image2.crop((left, top, right, bottom))

        if(IMU == "1"):
            im1.show()
        elif(IMU == "2"):
            im1.rotate(180).show()
        elif(IMU == "3"):
            im1.rotate(90).show()
        elif(IMU == "4"):
            im1.rotate(270).show()
        
    orientation(m1, m2)

    print (width)
    print (height)
