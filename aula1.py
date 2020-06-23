import numpy as np
import matplotlib.pyplot as plt
import cv2

image = cv2.imread('simp.png')
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

plt.figure(figsize=(30, 30))

plt.subplot(1, 2, 1)
plt.title("Identificando o Zelador")
plt.imshow(image)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

template = cv2.imread('zelador.png',0)

result = cv2.matchTemplate(gray, template, cv2.TM_CCOEFF)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

top_left = max_loc
bottom_right = (top_left[0] + 50, top_left[1] + 50)
cv2.rectangle(image, top_left, bottom_right, (0,0,255), 2)

plt.subplot(1, 2, 2)
plt.title("Zelador")
plt.imshow(image)
plt.show()
