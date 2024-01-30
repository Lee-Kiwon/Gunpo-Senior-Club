import cv2

img= cv2.imread('flower.jpg')

# 칼라로 출력
cv2.namedWindow('Show Image')
cv2.imshow('Show Image', img)


# 흑백으로 출력
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Show GrayScale Image", img_gray)

# 키보드 키를 누르기 전까지 계속 출력하기
cv2.waitKey(0)

# 파일 새로 저장
cv2.imwrite('image_save.jpg', img_gray)

# 키를 누르면 전체 다 닫힘

cv2.destroyAllWindows()