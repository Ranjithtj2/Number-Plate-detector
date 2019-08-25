import numpy as np
import cv2
import  imutils
import pandas as pd
import pytesseract 
pytesseract.pytesseract.tesseract_cmd='C:/Program Files (x86)/Tesseract-OCR/tesseract.exe'

i = cv2.imread('Car_Image99.jpeg')
i = imutils.resize(i, width=500)
cv2.imshow("plain image", i)
g = cv2.cvtColor(i, cv2.COLOR_BGR2GRAY)
g = cv2.bilateralFilter(g, 11, 17, 17)
e = cv2.Canny(g, 170, 200)

cn, n = cv2.findContours(e.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
cn=sorted(cn, key = cv2.contourArea, reverse = True)[:30] 
objectdect = None 
count = 0

for c in cn:
        peri = cv2.arcLength(c, True)
        apx = cv2.approxPolyDP(c, 0.02 * peri, True)
        x, y, w, h = cv2.boundingRect(apx)
        if len(apx) == 4: 
            objectdect = apx
            break

cv2.drawContours(i, [objectdect], -1, (0,255,0), 3)
cv2.imshow("Detected image", i)
crop_img = i[y:y+h, x:x+w]

config = ('-l eng --oem 1 --psm 3')

text = pytesseract.image_to_string(crop_img, config=config)
print(text)

data = {'v_number': [text]}
xl = pd.DataFrame(data, columns = ['v_number'])
xl.to_csv('data.csv')

cv2.waitKey(0)