from cv2 import cv2

r = "h"
h = 2
w = 3
dh = 0
dw = 0

if r == "h":
    dh = h * 600
    dw = w * 1024
elif r == "v":
    dh = h* 1024
    dw = w * 600

image = cv2.imread('pic/large.jpg')
(height, width) = image.shape[:2]


def crop1(im, n_width, n_height, width, height):

    image2 = im[int ((height - n_height)/2) : int (((height - n_height)/2) + n_height),  int ((width - n_width)/ 2) : int (((width - n_width)/ 2) + n_width)]
    return image2

def border_man(im, width, height, w_width, w_height):
     im = cv2.copyMakeBorder(im, int ((w_height - height)/2) , int ((w_height - height)/2) , int ((w_width - width)/2), int ((w_width - width)/2), cv2.BORDER_CONSTANT, None, 0)
     return im

if (width > dw):
    image = image[0:height, int((width - dw)/ 2) : int(((width - dw)/ 2) + dw)]
else:
    image = cv2.copyMakeBorder(image, 0, 0, int((dw - width)/2), int((dw - width)/2), cv2.BORDER_CONSTANT, None, 0)

if (height > dh):
    image = image[int((height - dh)/2) : int(((height - dh)/2) + dh), 0:width]
else:
    image = cv2.copyMakeBorder(image, int((dh - height)/2) , int((dh - height)/2), 0, 0, cv2.BORDER_CONSTANT, None, 0)


for i in range(0, w):
    for j in range(0, h):
        (height, width) = image.shape[:2]
        img = image[int(height/h) * j : int(height/h) * (j + 1), int(width/w) * i : int(width/w) * (i + 1)]
        cv2.imshow("single_display_image_produced", img)
        cv2.waitKey(0)
        # cv2.destroyAllWindows()
        cv2.imwrite("export/display" + str(j) + str(i) + ".jpg", img)



