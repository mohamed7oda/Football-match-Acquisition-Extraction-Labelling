!pip install google-search-results
import requests
from serpapi import GoogleSearch
!pip install opencv-python
import cv2
import numpy as np
import matplotlib.pyplot as plt

from PIL import Image

#step (1):

cap = cv2.VideoCapture("DataExample.mp4")

#step (2):

count = 0
frame_count= 0
while True:
  ret, frame = cap.read()
  if not ret:
    break
  output_path = f"/content/photo_{frame_count}.png"
  cv2.imwrite(output_path,frame)

  frame_count= frame_count + 1
  count = count + 1
  if count == 10:
    break



img = cv2.imread("photo_0.png")


img2= cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
plt.imshow(img2)
plt.show()
print("====================================================================")

#step************************* (3):
lower = 125,144,96
upper = 150,170,120


mask = cv2.inRange(img2,lower,upper)
plt.imshow(mask)
plt.show()
print("===================================================================")


#step********************** (4):

# Yellow team
lower2 = 154,116,52
upper2 = 245,195,145


mask2 = cv2.inRange(img2,lower2,upper2)
print("Yellow team: ")
plt.imshow(mask2)
plt.show()


for i in range(mask2.shape[1]):
    for j in range(mask2.shape[0]):
        if i<mask2.shape[1]-1 and j<mask2.shape[0]-1 and mask2[j][i]==255 and mask2[j][i+1]==255 and mask2[j+1][i]==255 and mask2[j][i+2]==255 and mask2[j+2][i]==255  :
            x=i
            y=j
            cv2.circle(mask2, (x, y), 35, (250,255,0), 2)

plt.imshow(mask2)
plt.show()


print("=====================================================================")

# Blue team
lower3 = 30,30,110
upper3 = 140,140,230


mask3 = cv2.inRange(img2,lower3,upper3)
print("Blue team: ")
plt.imshow(mask3)
plt.show()


for i in range(mask3.shape[1]):
    for j in range(mask3.shape[0]):
        if i<mask3.shape[1]-1 and j<mask3.shape[0]-1 and mask3[j][i]==255 and mask3[j][i+1]==255 and mask3[j+1][i+1]==255 and 0 <i < 435 and 25 < j < 180:
            x=i
            y=j
            cv2.circle(mask3, (x, y), 35, (130,255,0), 2)

plt.imshow(mask3)
plt.show()

print("=====================================================================")

#**************************step (5):

# Ball

lower4 = 150, 235, 190
upper4 = 255, 255, 238
mask4 = cv2.inRange(img2, lower4, upper4).copy()

plt.imshow(mask4)
plt.show()

for i in range(mask4.shape[1]):
    for j in range(mask4.shape[0]):
        if i<mask2.shape[1]-1 and j<mask4.shape[0]-1 and mask4[j][i]==255 and mask4[j][i+1]==255 and  280 <i < 320 and 80 < j < 120 :
            x=i
            y=j
            cv2.circle(mask4, (x, y), 30, (61,109,100), 2)

plt.imshow(mask4)
plt.show()
print("=====================================================================")



#**************step (6):

crops = []
width = img2.shape[1]
height = img2.shape[0]
cx = width // 4
cy = height // 3

# coordinate
blue_players = [(11, 149), (50, 87), (160, 36), (207, 158), (288, 84), (300, 104), (339, 133), (508, 194), (529, 178)]
yellow_players = [(184, 145), (225, 58), (247, 239), (297, 94), (320, 165), (332, 118), (422, 59), (424, 98), (461, 132), (507, 221)]

for j in range(3):
    for i in range(4):
        x = i * cx
        y = j * cy


        blue_count = 0
        for player in blue_players:
            if player[0] >= x and player[1] >= y and player[0] <= x + cx and player[1] <= y + cy:
                blue_count += 1


        yellow_count = 0
        for player in yellow_players:
            if player[0] >= x and player[1] >= y and player[0] <= x + cx and player[1] <= y + cy:
                yellow_count += 1

        crops.append({'crop': img2[y:y+cy, x:x+cx], 'blue_count': blue_count, 'yellow_count': yellow_count})

plt.figure(figsize=(12, 9))

for i in range(len(crops)):
    if i < 12:
        plt.subplot(3, 4, i+1)
        plt.imshow(crops[i]['crop'])
        plt.title(f"Blue: {crops[i]['blue_count']}, Yellow: {crops[i]['yellow_count']}")
        plt.axis('off')

plt.show()

#-------step3
cap = cv2.VideoCapture('DataExample.mp4')

for current_frame in range(10):
    ret, frame = cap.read()
    if not ret:
        break

    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    lower_white = np.array([116, 133, 80])
    upper_white = np.array([145, 154, 120])
    mask = cv2.inRange(frame_rgb, lower_white, upper_white)

    for i in range(mask.shape[0]):
        ct = 0
        max_ct = 0
        x, y = 0, 0
        for j in range(mask.shape[1]):
            if i < mask.shape[0] - 1 and j < mask.shape[1] - 1 and mask[i][j] == 255 and mask[i][j + 1] == 255:
                x = i
                y = j
                ct += 1
            else:
                if ct > max_ct:
                    max_ct = ct
                ct = 0
                if max_ct > 18:
                    cv2.ellipse(mask, (x, y - 10), (150, 50), 180, 0, 360, 255, 2)
                    max_ct = 0

    plt.imshow(mask)
    plt.show()

#step--3 draft 2
cap = cv2.VideoCapture('perfect.mp4')

for current_frame in range(5):
    ret, frame = cap.read()
    if not ret:
        break

    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    lower_white = np.array([130, 130, 25])
    upper_white = np.array([210, 195, 105])
    mask = cv2.inRange(frame_rgb, lower_white, upper_white)
    plt.imshow(mask)
    plt.show()
