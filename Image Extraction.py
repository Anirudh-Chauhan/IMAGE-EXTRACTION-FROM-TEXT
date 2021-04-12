import cv2
import numpy as np


image = cv2.imread('images (2).jpeg')
original = image.copy()
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (3, 3), 0)
canny = cv2.Canny(blurred, 120, 255, 1)
kernel = np.ones((5,5),np.uint8)
dilate = cv2.dilate(canny, kernel, iterations=1)

cont = cv2.findContours(dilate, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

if len(cont) == 2:
    conts = cont[0]
else:
    conts = cont[1]

print("Enter how many images you can see in the document: ")
total = int(input())
my_dict={}  
image_number = 0
for c in conts:
    x,y,w,h = cv2.boundingRect(c)
    cv2.rectangle(image, (x, y), (x + w, y + h), (36,255,12), 2)
    ROI = original[y:y+h, x:x+w]
    x = np.array(ROI)
    unique, counts = np.unique(x, return_counts=True)
    my_dict[image_number]= len(unique)
    image_number += 1
    
my_keys = sorted(my_dict, key=my_dict.get, reverse=True)[:total]
print(my_keys)

image_number = 0
for c in conts:
    x,y,w,h = cv2.boundingRect(c)
    cv2.rectangle(image, (x, y), (x + w, y + h), (36,255,12), 2)
    ROI = original[y:y+h, x:x+w]
    if image_number in my_keys:      
        cv2.imwrite("Result/ROI_{}.png".format(image_number), ROI)
    image_number += 1

cv2.waitKey(0)
