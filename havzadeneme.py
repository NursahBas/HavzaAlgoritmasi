# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 00:00:48 2021

@author: Nursah
"""

import cv2
import matplotlib.pyplot as plt
import numpy as np

camera = cv2.VideoCapture(1)
if camera.isOpened():
    _,frame  = camera.read()
    cv2.imwrite("karabiber_orj.jpeg",frame)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imwrite("karabiber1.jpeg",gray)
#resmi içe aktarıyoruz 
coin = cv2.imread ("karabiber1.jpeg")
plt.figure(), plt.imshow(coin),plt.axis("off")


#lpf: blurring
coin_blur= cv2.medianBlur(coin, 13 )
plt.figure(), plt.imshow(coin_blur), plt.axis("off")

#gray skala
coin_gray = cv2.cvtColor(coin_blur, cv2.COLOR_BGR2GRAY)
plt.figure(), plt.imshow(coin_gray , cmap ="gray"), plt.axis("off")

#binary threshold (arkasıyla farkı daha çok açmak için)
ret, coin_thresh = cv2.threshold(coin_gray, 75,255, cv2.THRESH_BINARY)
plt.figure(), plt.imshow(coin_thresh, cmap="gray"), plt.axis("off")

#kontur aşaması
contours,hierarchy = cv2.findContours(coin_thresh.copy(), cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)

for i in range (len (contours)):
    
    if hierarchy[0][i][3] == -1 :
        cv2.drawContours(coin, contours , i , (0,255,0) , 10)
plt.figure(), plt.imshow(coin), plt.axis("off")



##########################################
#son olarak 
coin = cv2.imread ("karabiber1.jpeg")
plt.figure(), plt.imshow(coin),plt.axis("off")
# detayları azaltıyoruz bluring işlemimiz
coin_blur= cv2.medianBlur(coin, 13 )
plt.figure(), plt.imshow(coin_blur), plt.axis("off")
#gray skala
coin_gray = cv2.cvtColor(coin_blur, cv2.COLOR_BGR2GRAY)
plt.figure(), plt.imshow(coin_gray , cmap ="gray"), plt.axis("off")


#binary threshold (arkasıyla farkı daha çok açmak için)
ret, coin_thresh = cv2.threshold(coin_gray, 65,255, cv2.THRESH_BINARY)
plt.figure(), plt.imshow(coin_thresh, cmap="gray"), plt.axis("off")

#erezyon ve genişleme açılması yapıyoruz gürültü azalması 

kernel = np.ones((3,3),np.uint8)
opening = cv2.morphologyEx(coin_thresh, cv2.MORPH_OPEN, kernel, iterations = 2)
plt.figure(), plt.imshow(opening, cmap="gray"), plt.axis("off")


#nesneler arası distance bulma
dist_transform =   cv2.distanceTransform(opening, cv2.DIST_L2, 5)
plt.figure(), plt.imshow(dist_transform, cmap="gray"), plt.axis("off")

# resmi küçültüyoruz aralarındaki bağı yok etmek için
ret, sure_foreground = cv2.threshold(dist_transform, 0.4*np.max(dist_transform),255,0)
plt.figure(), plt.imshow(sure_foreground, cmap="gray"), plt.axis("off")

#arka plan için resmi küçült bu sayede ön arka daha görünür bi hal tespit etmeye çalışıyoruz
sure_background = cv2.dilate(opening , kernel , iterations = 1)
sure_foreground = np.uint8(sure_foreground)
unknown = cv2.subtract(sure_background,sure_foreground)
plt.figure(), plt.imshow(unknown, cmap="gray"), plt.axis("off")


#bağlantı 
ret,marker = cv2.connectedComponents(sure_foreground)
marker = marker + 1
marker[unknown == 255]  = 0
plt.figure(), plt.imshow(marker, cmap="gray"), plt.axis("off")


#en son havza algoritması ile segmente ediyoruz 
marker = cv2.watershed(coin,marker)
plt.figure(), plt.imshow(marker, cmap="gray"), plt.axis("off")

#kontur aşaması
contours,hierarchy = cv2.findContours(marker.copy(), cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)

for i in range (len (contours)):
    
    if hierarchy[0][i][3] == -1 :
        cv2.drawContours(coin, contours , i , (255,0,0) ,2)
plt.figure(), plt.imshow(coin), plt.axis("off")
