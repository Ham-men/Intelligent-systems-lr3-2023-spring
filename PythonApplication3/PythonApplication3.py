import cv2
import imutils
import os

image = cv2.imread('img.jpg')
(h, w, d) = image.shape
print("width={}, height={}, depth={}".format(w, h, d))
cv2.imshow("Image", image)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
thresh = cv2.threshold(gray, 225, 255, cv2.THRESH_BINARY_INV)[1]
cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)

output = image.copy()
for c in cnts:
    cv2.drawContours(output, [c], -1, (240, 0, 159), 3)
text = "Количество найденных объектов = {}".format(len(cnts) )
cv2.putText(output, text, (100, 15), cv2.FONT_HERSHEY_COMPLEX, 0.6, (240, 0, 20), 2)

cv2.rectangle(output,(round(w/2)-20,round(h/2)-20),(round(w/2)+20,round(h/2)+20),(2,255,2),-1)
cv2.circle(output,(0,h), 6,(0,0,0), -1)
cv2.imshow("Contours", output)
cv2.waitKey(0)
