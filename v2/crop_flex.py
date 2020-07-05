from cv2 import cv2

def main(h, w, r, o, address):
    dh = 0
    dw = 0
    p = 0
    q = 0

    if o == "h":
        dh = h * 600
        dw = w * 1024
    elif o == "v":
        dh = h * 1024
        dw = w * 600

    image = cv2.imread(address)
    (height, width) = image.shape[:2]

    if (width > dw):
        image = image[0:height, int((width - dw)/ 2) : int(((width - dw)/ 2) + dw)]
    else:
        image = cv2.copyMakeBorder(image, 0, 0, int((dw - width)/2), int((dw - width)/2), cv2.BORDER_CONSTANT, None, 0)

    if (height > dh):
        image = image[int((height - dh)/2) : int(((height - dh)/2) + dh), 0:width]
    else:
        image = cv2.copyMakeBorder(image, int((dh - height)/2) , int((dh - height)/2), 0, 0, cv2.BORDER_CONSTANT, None, 0)

    if (r == "2"):
        for i in range(0, w):
            for j in range(0, h):
                (height, width) = image.shape[:2]
                img = image[int(height/h) * j : int(height/h) * (j + 1), int(width/w) * i : int(width/w) * (i + 1)]
                # cv2.imshow("single_display_image_produced", img)
                # cv2.waitKey(0)
                # cv2.destroyAllWindows()
                cv2.imwrite("export/display" + str(p) + str(q) + ".jpg", img)
                q = q + 1
            p = p + 1
            q = 0
    elif (r == "1"):
        for i in range(w, 0, -1):
            for j in range(h, 0, -1):
                (height, width) = image.shape[:2]
                img = image[int(height/h) * (j - 1) : int(height/h) * j, int(width/w) * (i - 1) : int(width/w) * i]
                # cv2.imshow("single_display_image_produced", img)
                # cv2.waitKey(0)
                # cv2.destroyAllWindows()
                cv2.imwrite("export/display" + str(p) + str(q) + ".jpg", img)
                q = q + 1
            p = p + 1
            q = 0
    elif (r == "3"):
        for i in range(0, w):
            for j in range(h, 0, -1):
                (height, width) = image.shape[:2]
                img = image[int(height/h) * (j - 1) : int(height/h) * j, int(width/w) * i : int(width/w) * (i + 1)]
                # cv2.imshow("single_display_image_produced", img)
                # cv2.waitKey(0)
                # cv2.destroyAllWindows()
                cv2.imwrite("export/display" + str(p) + str(q) + ".jpg", img)
                q = q + 1
            p = p + 1
            q = 0
    elif (r == "4"):
        for i in range(w, 0, -1):
            for j in range(0, h):
                (height, width) = image.shape[:2]
                img = image[int(height/h) * j : int(height/h) * (j + 1), int(width/w) * (i - 1) : int(width/w) * i]
                # cv2.imshow("single_display_image_produced", img)
                # cv2.waitKey(0)
                # cv2.destroyAllWindows()
                cv2.imwrite("export/display" + str(p) + str(q) + ".jpg", img)
                q = q + 1
            p = p + 1
            q = 0




