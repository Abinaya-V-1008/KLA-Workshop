import cv2
#print(cv2.__version__)
import json
f=open('input.json')
data=json.load(f)
for i in data['die']:
    print(i)

img = cv2.imread('wafer_image_1.png')
print(img.shape)
print(img)

#extracting single pixel
print(img[0][1])