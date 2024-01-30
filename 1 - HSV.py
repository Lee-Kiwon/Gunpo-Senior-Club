import numpy as np
import cv2

# BGR순서 (파랑색)
color = [255, 0, 0]

# 한 픽셀로 구성된 이미지로 변환
pixel = np.uint8([[color]])

# hsv 색공간으로 변환
hsv = cv2.cvtColor(pixel, cv2.COLOR_BGR2HSV)
hsv = hsv[0][0]

# 이거로 파란색이 hsv로 변환하면 120인걸 찾음
print("bgr : ", color)
print("hsv", hsv)







# hsv 색공간으로 특정색 검출
img_color = cv2.imread("hsv.jpg")
height, width = img_color.shape[:2]

img_hsv = cv2.cvtColor(img_color, cv2.COLOR_BGR2HSV)

# 너무 밝거나 너무 어두운 것 고려
lower_blue = (120-10, 30, 30)
upper_blue = (120+10, 255, 255)

# 특정 물체 추출
img_mask = cv2.inRange(img_hsv, lower_blue, upper_blue)

# 결과
img_result = cv2.bitwise_and(img_color, img_color, mask = img_mask)

cv2.imshow('img_color', img_color)
cv2.imshow('img_mask', img_mask)
cv2.imshow('img_result', img_result)

cv2.waitKey(0)
cv2.destroyAllWindows()