#!/usr/bin/env python
# coding: utf-8

# In[ ]:



import cv2
from rmn import RMN


image = cv2.imread("demo.png")
m = RMN()
results = m.detect_emotion_for_single_frame(image)
print(results)
image = m.draw(image, results)
cv2.imwrite("output.png", image)

