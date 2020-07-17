import cv2
from pytesseract import image_to_string

def image_to_text(frame):
    return image_to_string(frame)

cam = cv2.VideoCapture("output.mp4")
value = 0
flag = ""
while 1:
    frame = cam.read()[1]
    cv2.imwrite("frame"+str(value)+".png",frame)
    flag += image_to_text(frame)
    cv2.waitKey(1)
    value += 1
    if value == 4:
        break
print(flag)
cam.release()
cv2.destroyAllWindows()
